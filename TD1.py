import numpy as np


def dummy(N):
    assert (N > 0)
    x = np.arange(N)
    print(x)
    return np.array([x[::2].sum(), x[1::2].sum()])


def histogram(data, lower, upper, classes):
    h = []
    step = (upper - lower) // classes
    for i in range(lower, upper, step):
        h.append((float(i), len(data[(data >= i) & (data < i + step)])))
    return h


nb_samples = 10
data = np.random.randint(0, 20, nb_samples)
histo = histogram(data, 0, 20, 5)
print(data)
print(histo)
print(np.sum([couple[1] for couple in histo]))
assert np.sum([couple[1] for couple in histo]) == nb_samples
