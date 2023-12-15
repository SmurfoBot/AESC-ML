import numpy as np


def prod_non_zero_diag(x):
    return np.prod(np.diag(x)[np.diag(x) != 0])


def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))


def max_after_zero(x):
    return np.max(x[1:][x[:-1] == 0])


def convert_image(img, coefs):
    return np.dot(img, coefs)


def run_length_encoding(x):
    return (x[np.nonzero(np.diff(np.concatenate((x, np.array([x[-1] - 1])))))],
            np.diff(np.nonzero(np.diff(np.concatenate((np.array([0]), x, np.array([x.shape[0]])))))))


def pairwise_distance(x, y):
    return np.linalg.norm(x[:, np.newaxis] - y, axis=2)