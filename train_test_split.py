import numpy as np

def train_test_split(data, test_ratio):
    np.random.seed(42)
    shuffled_test_size= np.random.permutation(len(data))
    test_size= int(len(data) * test_ratio)
    test_indices= shuffled_test_size[: test_size]
    train_indices= suffled_test_size[test_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
