#!/usr/bin/env python3
"""Fail-closed structural checks for the published adversarial-attack audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = (
    "MachineLearning-Nerd/"
    "icml26-consistent-adversarial-attacks-linear-classification"
)
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = (
    "37579156+MachineLearning-Nerd@users.noreply.github.com"
)
EXPECTED_SOURCE_HTML_SHA = (
    "83b475d685ce1c7b0988d027f3ad3d8e0ff95afeeb583bdd58f0a31bca7f8696"
)
EXPECTED_SOURCE_PDF_SHA = (
    "d57224430f16e29eca731470f2a756428aa2f53b2c9001dfb3a04ccd1d4f23ce"
)
EXPECTED_LOCK_SHA = (
    "b2508cf35b49d001059c7e47e99a3f3b8ad7837209855298d1684391455583d1"
)
EXPECTED_SCIENCE_SHA = "3688690d5ee0a644b06807b0dd6d0525be19edcc"
EXPECTED_BRANCHES = {
    "main",
    "audit/claim-4-falsification-eligibility",
    "audit/claim-4-mechanism-decomposition",
    "audit/claim-4-scaling-ambiguity",
    "audit/latent-theorem-integrity",
    "audit/metric-quantifier-specification",
    "audit/proposition-1-baseline",
    "audit/theorem-3-1-printed-formula",
    "release/evaluator-visible-candidate",
}
EXPECTED_CLAIMS = {
    "C1": "VERIFIED",
    "C2": "FALSIFIED",
    "C3": "FALSIFIED",
    "C4": "BLOCKED",
    "C5": "FALSIFIED",
}
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "REPORT.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "BRANCH_AUDIT.md",
    "ENVIRONMENT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
    "AUTONOMOUS_STATE.json",
}
EXPECTED_AUDIT_FILES = REQUIRED_FILES - {"AUTONOMOUS_STATE.json"}
EXPECTED_EVIDENCE_FILES = {
    "evidence/results.json",
    "evidence/checker-output.json",
    "evidence/control-output.json",
    "evidence/runtime.csv",
    "candidate_space/current/data/results.json",
    "candidate_space/current/data/checker-output.json",
    "candidate_space/current/data/control-output.json",
    "candidate_space/current/data/runtime.csv",
    "reports/reproduction/report.md",
    "release/visibility-matrix.md",
    "release/release-report.md",
    "repro/src/core.py",
    "repro/src/theorem31.py",
    "repro/src/latent_audit.py",
    "repro/src/quantifier_audit.py",
    "repro/src/release_audit.py",
    "repro/src/verify.py",
}
EXPECTED_EVIDENCE_DIRS = {
    ".openresearch/artifacts/claim_1",
    ".openresearch/artifacts/claim_2",
    ".openresearch/artifacts/claim_3",
    ".openresearch/artifacts/claim_4",
    ".openresearch/artifacts/claim_5",
    "candidate_space/current/code",
    "candidate_space/current/data",
    "candidate_space/current/audits/claim_1",
    "candidate_space/current/audits/claim_2",
    "candidate_space/current/audits/claim_3",
    "candidate_space/current/audits/claim_4",
    "candidate_space/current/audits/claim_5",
}
for _claim in range(1, 6):
    EXPECTED_EVIDENCE_FILES.update(
        {
            f".openresearch/artifacts/claim_{_claim}/{name}"
            for name in (
                "claim_contract.json",
                "method.md",
                "source_audit.md",
                "limitations.md",
                "raw_results.json",
                "checker-output.json",
                "negative-control-output.json",
            )
        }
    )
for _path in (
    ".openresearch/artifacts/claim_4/route_2.md",
    ".openresearch/artifacts/claim_4/route_3.md",
    ".openresearch/artifacts/claim_4/route_4.md",
    ".openresearch/artifacts/claim_5/route_2.md",
):
    EXPECTED_EVIDENCE_FILES.add(_path)

CONTENT_ADDRESSED_PATHS = {
    *EXPECTED_AUDIT_FILES - {"EVIDENCE_MANIFEST.json"},
    "pyproject.toml",
    "uv.lock",
    *EXPECTED_EVIDENCE_FILES,
}


def fail(message: str) -> None:
    raise AssertionError(message)


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def read_json(relative_path: str) -> object:
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(relative_path: str) -> str:
    digest = hashlib.sha256()
    with (ROOT / relative_path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_branches() -> set[str]:
    refs = run(
        "git",
        "for-each-ref",
        "refs/heads",
        "--format=%(refname:strip=2)",
    )
    return {ref.strip() for ref in refs.splitlines() if ref.strip()}


def remote_branches() -> set[str]:
    prefix = "refs/remotes/origin/"
    refs = run(
        "git",
        "for-each-ref",
        "refs/remotes/origin",
        "--format=%(refname)",
    )
    return {
        ref.strip()[len(prefix):]
        for ref in refs.splitlines()
        if ref.strip().startswith(prefix)
        and ref.strip() != prefix + "HEAD"
    }


def verify_remote() -> None:
    remote = run("git", "config", "--get", "remote.origin.url").strip()
    normalized = remote.removesuffix(".git").rstrip("/")
    if not normalized.endswith(EXPECTED_REPOSITORY):
        fail(f"origin is {remote!r}, expected {EXPECTED_REPOSITORY!r}")


def verify_branch_tips() -> None:
    remote = remote_branches()
    if remote != EXPECTED_BRANCHES:
        fail(f"remote branch set is {sorted(remote)!r}")
    local = local_branches()
    if "main" not in local:
        fail("local main branch is missing")
    for branch in EXPECTED_BRANCHES:
        remote_tip = run(
            "git",
            "rev-parse",
            f"refs/remotes/origin/{branch}",
        ).strip()
        if branch in local:
            local_tip = run(
                "git",
                "rev-parse",
                f"refs/heads/{branch}",
            ).strip()
            if local_tip != remote_tip:
                fail(f"local and origin tips differ for {branch}")
    head = run("git", "symbolic-ref", "refs/remotes/origin/HEAD").strip()
    if head != "refs/remotes/origin/main":
        fail(f"origin HEAD is {head!r}, expected origin/main")


def verify_history() -> None:
    records = run(
        "git",
        "log",
        "--all",
        "--format=%an%x00%ae%x00%cn%x00%ce",
    ).splitlines()
    if not records:
        fail("no reachable commits")
    expected = (
        f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}\x00"
        f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}"
    )
    unexpected = sorted({record for record in records if record != expected})
    if unexpected:
        fail(f"non-canonical reachable identities: {unexpected}")
    if "co-authored-by:" in run("git", "log", "--all", "--format=%B").lower():
        fail("co-author trailer found")
    if int(run("git", "rev-list", "--count", "--all").strip()) < 13:
        fail("historical evidence commits are missing")
    if run(
        "git",
        "for-each-ref",
        "refs/original",
        "--format=%(refname)",
    ).strip():
        fail("temporary refs/original remain")
    refs = run("git", "for-each-ref", "--format=%(refname)").splitlines()
    if any("orx/" in ref or ref.endswith("/orx") for ref in refs):
        fail("legacy orx ref remains")


def verify_manifest() -> None:
    manifest = read_json("EVIDENCE_MANIFEST.json")
    if not isinstance(manifest, dict):
        fail("manifest must be a JSON object")
    if manifest.get("repository") != EXPECTED_REPOSITORY:
        fail("manifest repository marker is wrong")
    if manifest.get("claim_statuses") != EXPECTED_CLAIMS:
        fail("manifest claim statuses are wrong")
    if set(manifest.get("required_audit_files", [])) != EXPECTED_AUDIT_FILES:
        fail("manifest audit-file list is wrong")
    if set(manifest.get("required_evidence_files", [])) != EXPECTED_EVIDENCE_FILES:
        fail("manifest evidence-file list is wrong")
    if set(manifest.get("required_evidence_directories", [])) != EXPECTED_EVIDENCE_DIRS:
        fail("manifest evidence-directory list is wrong")
    branch_record = manifest.get("branches", {})
    if set(branch_record.get("expected_final", [])) != EXPECTED_BRANCHES:
        fail("manifest branch set is wrong")
    if branch_record.get("historical_remote_branch_count") != 9:
        fail("manifest historical branch count is wrong")
    if branch_record.get("legacy_prefixes_removed") != ["orx/"]:
        fail("manifest legacy-prefix record is wrong")
    if manifest.get("attribution", {}).get("email") != CANONICAL_EMAIL:
        fail("manifest attribution is wrong")
    artifacts = manifest.get("content_addressed_artifacts", [])
    if {item.get("path") for item in artifacts} != CONTENT_ADDRESSED_PATHS:
        fail("manifest content-addressed path list is wrong")
    for item in artifacts:
        relative_path = item.get("path")
        expected_hash = item.get("sha256")
        if not isinstance(relative_path, str) or not isinstance(expected_hash, str):
            fail("malformed content-addressed artifact")
        if not (ROOT / relative_path).is_file():
            fail(f"missing content-addressed artifact: {relative_path}")
        if sha256(relative_path) != expected_hash:
            fail(f"artifact hash mismatch: {relative_path}")


def verify_evidence() -> None:
    manifest = read_json("EVIDENCE_MANIFEST.json")
    for relative_path in manifest.get("required_evidence_files", []):
        if not (ROOT / relative_path).is_file():
            fail(f"missing required evidence file: {relative_path}")
    for relative_path in manifest.get("required_evidence_directories", []):
        if not (ROOT / relative_path).is_dir():
            fail(f"missing required evidence directory: {relative_path}")

    for filename in (
        "results.json",
        "checker-output.json",
        "control-output.json",
        "runtime.csv",
    ):
        canonical = ROOT / "evidence" / filename
        mirror = ROOT / "candidate_space/current/data" / filename
        if canonical.read_bytes() != mirror.read_bytes():
            fail(f"evaluator evidence mirror differs: {filename}")

    results = read_json("evidence/results.json")
    if not isinstance(results, dict):
        fail("results must be a JSON object")
    if results.get("paper") != "arXiv:2506.12454v1":
        fail("results paper marker is wrong")
    if results.get("paper_html_sha256") != EXPECTED_SOURCE_HTML_SHA:
        fail("results HTML source hash is wrong")
    if results.get("paper_pdf_sha256") != EXPECTED_SOURCE_PDF_SHA:
        fail("results PDF source hash is wrong")
    if results.get("science_git_sha") != EXPECTED_SCIENCE_SHA:
        fail("results science revision is wrong")
    if results.get("fixed_command") != (
        "uv sync --frozen && .venv/bin/python repro/src/verify.py"
    ):
        fail("results fixed command is wrong")
    if results.get("uv_lock_sha256") != EXPECTED_LOCK_SHA:
        fail("results lock hash is wrong")
    if results.get("seeds") != [1031, 2081, 4093, 8179]:
        fail("results seeds are wrong")

    claims = results.get("claims", {})
    c1 = claims.get("1", {})
    if {
        c1.get("status"),
        c1.get("agreement"),
        c1.get("trials"),
        c1.get("feasible"),
        c1.get("infeasible"),
        c1.get("mutation_disagreements"),
    } != {"VERIFIED", 400, 200, 20}:
        fail("Claim 1 evidence values are wrong")
    c2 = claims.get("2", {})
    if (
        c2.get("status") != "FALSIFIED"
        or c2.get("printed_robust") != 0.5
        or c2.get("definition_robust") != 0.6914624612740131
        or c2.get("samples") != 4000000
    ):
        fail("Claim 2 evidence values are wrong")
    c3 = claims.get("3", {})
    if (
        c3.get("status") != "FALSIFIED"
        or c3.get("missing_primal_definitions") != ["P", "V", "m", "q"]
        or c3.get("appendix_conflicts") != ["hat_P", "hat_V", "hat_q"]
        or c3.get("repaired_control_closed") is not True
    ):
        fail("Claim 3 evidence values are wrong")
    c4 = claims.get("4", {})
    if (
        c4.get("status") != "BLOCKED"
        or c4.get("routes_completed") != 4
        or c4.get("decomposition_cases") != 2000000
        or c4.get("decomposition_residual") != 0
        or c4.get("eligible_counterexamples") != 0
    ):
        fail("Claim 4 evidence values are wrong")
    c5 = claims.get("5", {})
    if (
        c5.get("status") != "FALSIFIED"
        or c5.get("samples") != 2000000
        or c5.get("correlations") != [-0.75, -0.25, 0.25, 0.75]
        or c5.get("omitted_half_strip_counts")
        != [95578, 95931, 95398, 95540]
    ):
        fail("Claim 5 evidence values are wrong")

    checker = read_json("evidence/checker-output.json")
    if (
        checker.get("claim_1", {}).get("passed") is not True
        or checker.get("claim_2", {}).get("passed") is not True
        or checker.get("claim_3", {}).get("passed") is not True
        or checker.get("claim_4", {}).get("final_status") != "BLOCKED"
        or checker.get("claim_5", {}).get("passed") is not True
    ):
        fail("checker output is not the expected passing certificate")

    control = read_json("evidence/control-output.json")
    expected_controls = {
        "claim_1_full_norm_mutation": "REJECTED_AS_EXPECTED",
        "claim_2_zero_budget": "NOT_REJECTED_AS_EXPECTED",
        "claim_3_appendix_consistent_repair": "NOT_REJECTED_AS_EXPECTED",
        "claim_4_complete_contract": "ACCEPTED_AS_EXPECTED",
        "claim_4_drop_clean_error_mutation": "REJECTED_AS_EXPECTED",
        "claim_4_fully_pinned_opposite_trend": "ACCEPTED_AS_EXPECTED",
        "claim_5_zero_threshold": "NOT_REJECTED_AS_EXPECTED",
    }
    if control != expected_controls:
        fail("negative-control output is wrong")


def verify_ledgers_and_state() -> None:
    claims = read_json("claims.json")
    state = read_json("AUTONOMOUS_STATE.json")
    if not isinstance(claims, dict) or not isinstance(state, dict):
        fail("claim ledger and state must be JSON objects")
    if {
        row.get("id"): row.get("status") for row in claims.get("claims", [])
    } != EXPECTED_CLAIMS:
        fail("claims.json statuses are wrong")
    if claims.get("repository") != EXPECTED_REPOSITORY:
        fail("claims.json repository marker is wrong")
    paper = claims.get("paper", {})
    if paper.get("html_sha256") != EXPECTED_SOURCE_HTML_SHA:
        fail("claims.json HTML source hash is wrong")
    if paper.get("pdf_sha256") != EXPECTED_SOURCE_PDF_SHA:
        fail("claims.json PDF source hash is wrong")
    if state.get("target_github_repository") != (
        "https://github.com/" + EXPECTED_REPOSITORY
    ):
        fail("state repository marker is wrong")
    if state.get("canonical_branch") != "main":
        fail("state canonical branch is wrong")
    identity = state.get("canonical_identity", {})
    if identity.get("name") != CANONICAL_NAME:
        fail("state canonical identity is wrong")
    if identity.get("email") != CANONICAL_EMAIL:
        fail("state canonical email is wrong")
    if state.get("paper_html_sha256") != EXPECTED_SOURCE_HTML_SHA:
        fail("state HTML source hash is wrong")
    if state.get("paper_pdf_sha256") != EXPECTED_SOURCE_PDF_SHA:
        fail("state PDF source hash is wrong")
    if state.get("science_evidence_commit") != EXPECTED_SCIENCE_SHA:
        fail("state science revision is wrong")
    if state.get("historical_branch_count") != 8:
        fail("state historical branch count is wrong")
    if set(state.get("expected_branches", [])) != EXPECTED_BRANCHES:
        fail("state branch set is wrong")
    if state.get("phase") not in {
        "dossier_ready_for_publication",
        "dossier_published",
    }:
        fail("state phase is not a dossier phase")


def verify_documentation() -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            fail(f"required file is missing: {relative_path}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "BRANCH_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "EVIDENCE_MANIFEST.json",
        "VERIFIED",
        "FALSIFIED",
        "BLOCKED",
        "verify_final.py",
    ):
        if marker not in readme:
            fail(f"README is missing marker {marker!r}")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    for marker in ("EVIDENCE_MANIFEST.json", "verify_final.py", "raw evidence boundary"):
        if marker not in status:
            fail(f"STATUS is missing marker {marker!r}")
    branch_audit = (ROOT / "BRANCH_AUDIT.md").read_text(encoding="utf-8")
    if branch_audit.count("| orx/") != 8:
        fail("branch migration table is incomplete")
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text(encoding="utf-8")
    for source_hash in (EXPECTED_SOURCE_HTML_SHA, EXPECTED_SOURCE_PDF_SHA):
        if source_hash not in source_audit:
            fail("source audit hash is missing")
    thanks = (ROOT / "AUTHOR_THANK_YOU.md").read_text(encoding="utf-8")
    for author in ("Matteo Vilucchio", "Lenka Zdeborová", "Bruno Loureiro"):
        if author not in thanks:
            fail(f"author thanks is missing {author}")


def main() -> int:
    verify_documentation()
    verify_remote()
    verify_branch_tips()
    verify_history()
    verify_manifest()
    verify_evidence()
    verify_ledgers_and_state()
    print("PASS: published adversarial-attack audit state is structurally verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
