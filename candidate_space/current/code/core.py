from __future__ import annotations

import math

import numpy as np


def orthogonal_component(w_star: np.ndarray, w_hat: np.ndarray) -> np.ndarray:
    return w_hat - w_star * (np.dot(w_star, w_hat) / np.dot(w_star, w_star))


def proposition_condition(
    w_star: np.ndarray, w_hat: np.ndarray, x: np.ndarray, epsilon: float
) -> bool:
    w_perp = orthogonal_component(w_star, w_hat)
    return epsilon * np.linalg.norm(w_perp) >= abs(np.dot(w_hat, x))


def feasibility_certificate(
    w_star: np.ndarray, w_hat: np.ndarray, x: np.ndarray, epsilon: float
) -> dict[str, float | bool]:
    w_perp = orthogonal_component(w_star, w_hat)
    norm = float(np.linalg.norm(w_perp))
    margin = float(np.dot(w_hat, x))
    maximum_shift = epsilon * norm
    feasible = maximum_shift > abs(margin)

    if norm == 0:
        delta = np.zeros_like(w_hat)
    else:
        delta = -math.copysign(epsilon, margin) * w_perp / norm

    return {
        "feasible": feasible,
        "maximum_shift": maximum_shift,
        "margin_abs": abs(margin),
        "delta_norm": float(np.linalg.norm(delta)),
        "target_inner_product": float(np.dot(w_star, delta)),
        "attacked_margin": float(np.dot(w_hat, x + delta)),
    }


def mutated_condition(
    w_star: np.ndarray, w_hat: np.ndarray, x: np.ndarray, epsilon: float
) -> bool:
    del w_star
    return epsilon * np.linalg.norm(w_hat) >= abs(np.dot(w_hat, x))
