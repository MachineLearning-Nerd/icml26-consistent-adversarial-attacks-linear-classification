from __future__ import annotations

import ast
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


JUDGED_HASHES = {
    ".gitattributes": "11ad7efa24975ee4b0c3c3a38ed18737f0658a5f75a0a96787b576a78a023361",
    "README.md": "ffa64a48d5a8362da246db11cb515313d3192509833749c6db3a7bb1b4845d38",
    "bucket-icon.svg": "d1c28fc0a4e07f2688d013f576cf76ffc422d278d56a52a82989e0b93b3b3964",
    "index.html": "feb8f4111c550ac7127ab1ec75ec7e157bf47eac997b0aacc00bafc06ea60f90",
    "logbook.css": "64e1de4358c79ec0d5f2697c56f98258c025e992c94ad7b3b7801739222ca41d",
    "logbook.js": "69d73869184f936613668569980f31984be65229e77c4df4ba9604d3de70c02b",
    "logbook.json": "00a3173632ef26c81e233b617a9f147274621e5ca13babbcae87b0d912b7fa65",
    "pages/claims/page.md": "64e9756d4c043c18125b14e0f813bd54a8bb036d0e0dfd1846b6e81da845f5a3",
    "pages/conclusion/page.md": "fe6e4e2293c93f269e52abc970dfa23030d4ccc7c7ab0b7a3de0ae0e86b741de",
    "pages/evidence/page.md": "b3fb2794b2d49af1ee20e3014c5b8967d458e490a65af331161524890f74e54f",
    "pages/index.md": "fe441ee896ab1e4e00d45f34914c91516fbb0b6549c2c2d5e1300a2a27f9b618",
    "pages/overview/page.md": "3531b5df60b2babf262692314ea639b4e9456734e7c046cf1f6d5228b1bbaff6",
    "pages/verification-run/page.md": "b38cdf87050e1a6173508ca92008cc4f02588ad4e76e0dd634527cd1d0be0fc9",
    "style.css": "789bfd541c9f06658ac410d968e9c39fa8c63a48a08643b36071b984c699a9f4",
    "trackio-logo-light.png": "a6eb72253c0128ce79b526a86b7943eed37beec186b5f57ff6c1701d0e9ff596",
    "trackio-logo.png": "3e3792061d4d095759da30d7cfe7f14b621901793cd4d677b61b2896f5bf472b",
    "trackio-wordmark-dark.png": "71da94795855710d214801eb9b9b7b8898e9a8757abac0e22966a0531bbb2f4f",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_release(root: Path) -> dict[str, object]:
    candidate = root / "candidate_space"
    historical = candidate / "historical" / "judged-5157b05f"
    historical_checks = {
        path: historical.joinpath(path).is_file()
        and sha256(historical / path) == expected
        for path, expected in JUDGED_HASHES.items()
    }
    old_file_set_subset = all(candidate.joinpath(path).is_file() for path in JUDGED_HASHES)

    logbook = json.loads((candidate / "logbook.json").read_text())
    current_first = (
        logbook["root"]["children"][0]["slug"] == "current-verification"
        and "start here" in logbook["root"]["children"][0]["title"].lower()
    )
    historical_labeled = all(
        "Historical rejected baseline" in child["title"]
        for child in logbook["root"]["children"][1:]
    )

    current_page = candidate / "pages" / "current-verification" / "page.md"
    current_text = current_page.read_text()
    links = re.findall(r"\[[^\]]+\]\(([^)#]+)\)", current_text)
    missing_links = sorted(
        link
        for link in links
        if not (current_page.parent / link).resolve().is_file()
    )
    required_phrases = [
        "Claim 1 — VERIFIED",
        "Claim 2 — FALSIFIED as printed",
        "Claim 3 — FALSIFIED as printed",
        "Claim 4 — BLOCKED after four routes",
        "Claim 5 — FALSIFIED as printed",
        "Visibility matrix",
        "uv sync --frozen && .venv/bin/python repro/src/verify.py",
    ]
    missing_phrases = [phrase for phrase in required_phrases if phrase not in current_text]

    allowlist = [
        line.strip()
        for line in (root / "release" / "upload-allowlist.txt").read_text().splitlines()
        if line.strip()
    ]
    allowlist_missing = [path for path in allowlist if not candidate.joinpath(path).is_file()]
    text_suffixes = {
        ".md", ".json", ".csv", ".py", ".toml", ".lock", ".svg",
        ".html", ".css", ".js", ".txt", ".sha256",
    }
    non_text_allowlist = [
        path
        for path in allowlist
        if Path(path).suffix not in text_suffixes and Path(path).name != ".gitattributes"
    ]
    duplicate_allowlist = len(allowlist) != len(set(allowlist))

    manifest_relative = "current/release/upload-manifest.sha256"
    manifest_lines = [
        line.split("  ", 1)
        for line in (root / "release" / "upload-manifest.sha256").read_text().splitlines()
        if line.strip()
    ]
    manifest = {path: digest for digest, path in manifest_lines}
    expected_manifest_paths = set(allowlist) - {manifest_relative}
    manifest_paths_exact = set(manifest) == expected_manifest_paths
    manifest_hash_failures = sorted(
        path
        for path in expected_manifest_paths & set(manifest)
        if sha256(candidate / path) != manifest[path]
    )

    red_team_text = (candidate / "current" / "release" / "red-team.md").read_text()
    red_team_complete = all(
        phrase in red_team_text
        for phrase in ["## Round 1", "Release was rejected", "## Round 2 after fixes", "Files opened"]
    )

    json_paths = [
        candidate / "logbook.json",
        candidate / "current" / "data" / "results.json",
        candidate / "current" / "data" / "checker-output.json",
        candidate / "current" / "data" / "control-output.json",
    ]
    parsed_json = all(json.loads(path.read_text()) is not None for path in json_paths)
    svg_paths = sorted((candidate / "current" / "images").glob("*.svg"))
    svg_valid = len(svg_paths) == 5 and all(ET.parse(path) for path in svg_paths)

    notebook = root / "notebooks" / "reproduction.py"
    ast.parse(notebook.read_text())
    notebook_structural_check = (
        "import marimo" in notebook.read_text()
        and "app = marimo.App" in notebook.read_text()
        and "if __name__ == \"__main__\"" in notebook.read_text()
    )
    marimo_check = json.loads(
        (candidate / "current" / "release" / "marimo-check.json").read_text()
    )
    marimo_check_passed = (
        marimo_check["command"] == "marimo check notebooks/reproduction.py"
        and marimo_check["exit_code"] == 0
    )
    figure_check = json.loads(
        (candidate / "current" / "release" / "figure-check.json").read_text()
    )
    figure_check_passed = (
        figure_check["result"] == "PASS" and len(figure_check["files"]) == 5
    )

    secret_patterns = [
        re.compile(r"hf_[A-Za-z0-9]{20,}"),
        re.compile(r"ghp_[A-Za-z0-9]{20,}"),
        re.compile(r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----"),
    ]
    secret_hits = []
    for relative in allowlist:
        text = candidate.joinpath(relative).read_text(errors="replace")
        if any(pattern.search(text) for pattern in secret_patterns):
            secret_hits.append(relative)

    results = json.loads((candidate / "current" / "data" / "results.json").read_text())
    verdicts_match = {
        "1": results["claims"]["1"]["status"] == "VERIFIED",
        "2": results["claims"]["2"]["status"] == "FALSIFIED",
        "3": results["claims"]["3"]["status"] == "FALSIFIED",
        "4": results["claims"]["4"]["status"] == "BLOCKED"
        and results["claims"]["4"]["routes_completed"] == 4,
        "5": results["claims"]["5"]["status"] == "FALSIFIED",
    }
    passed = (
        all(historical_checks.values())
        and old_file_set_subset
        and current_first
        and historical_labeled
        and not missing_links
        and not missing_phrases
        and not allowlist_missing
        and not non_text_allowlist
        and not duplicate_allowlist
        and manifest_paths_exact
        and not manifest_hash_failures
        and red_team_complete
        and parsed_json
        and svg_valid
        and notebook_structural_check
        and marimo_check_passed
        and figure_check_passed
        and not secret_hits
        and all(verdicts_match.values())
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "judged_revision": "5157b05fbbbad2885cd379658d7b58e688863e94",
        "historical_hashes_exact": all(historical_checks.values()),
        "historical_hash_failures": sorted(
            path for path, ok in historical_checks.items() if not ok
        ),
        "old_file_set_subset": old_file_set_subset,
        "current_navigation_first": current_first,
        "historical_navigation_labeled": historical_labeled,
        "current_page_missing_links": missing_links,
        "current_page_missing_phrases": missing_phrases,
        "allowlist_count": len(allowlist),
        "allowlist_missing": allowlist_missing,
        "allowlist_non_text": non_text_allowlist,
        "allowlist_duplicates": duplicate_allowlist,
        "manifest_excludes_only_itself": manifest_paths_exact,
        "manifest_hash_failures": manifest_hash_failures,
        "red_team_two_pass_complete": red_team_complete,
        "json_valid": parsed_json,
        "svg_count": len(svg_paths),
        "svg_xml_valid": svg_valid,
        "notebook_structural_check": notebook_structural_check,
        "marimo_check_command": marimo_check["command"],
        "marimo_check_exit_code": marimo_check["exit_code"],
        "figure_render_check": figure_check["result"],
        "secret_hits": secret_hits,
        "verdicts_match": verdicts_match,
        "verifier_passed": passed,
    }
