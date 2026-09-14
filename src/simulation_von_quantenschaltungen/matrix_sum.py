import numpy as np


def matrix_sum(matrices: list[np.ndarray]) -> np.ndarray:
    if not matrices:
        raise ValueError("matrix_sum requires at least one matrix")

    sum = matrices[0]
    for matrix in matrices[1:]:
        sum = sum + matrix

    return sum
