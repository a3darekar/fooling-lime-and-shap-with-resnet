def one_hot_encode(y):
    y_hat_one_hot = np.zeros((len(y), 2))
    y_hat_one_hot[np.arange(len(y)), y] = 1
    return y_hat_one_hot
