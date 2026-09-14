import numpy as np


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    if not matrices:
        raise ValueError("matrix_product requires at least one matrix")

    product = matrices[0]
    for matrix in matrices[1:]:
        product = product @ matrix

    return product
