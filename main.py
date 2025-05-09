import numpy as np


X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])


y = np.array([0, 1, 1, 1])


class Perceptron:
    def __init__(self, learning_rate=0.1, n_iter=10):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self._activation_function(linear_output)
                error=y[idx] - y_predicted
                if error !=0:

                    # LR : the % of how much the LR & WE differed activ we
                    update = self.learning_rate * error
                    self.weights += update * x_i
                    self.bias += update

    def _activation_function(self, x):
        return np.where(x >= 0, 1, 0)

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self._activation_function(linear_output)


# create perceptron
perceptron = Perceptron(learning_rate=0.1, n_iter=3)

# train
perceptron.fit(X, y)

# examine
predictions = perceptron.predict(X)
print("pre:", predictions)
