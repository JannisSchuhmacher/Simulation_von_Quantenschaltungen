import numpy as np


def matrix_power(matrix: np.ndarray, n: int) -> np.ndarray:
	if n < 0:
		raise ValueError("matrix_power requires a nonnegative exponent")

	if n == 0:
		return np.eye(matrix.shape[0], dtype=matrix.dtype)

	power = matrix
	for _ in range(n - 1):
		power = power @ matrix

	return power
