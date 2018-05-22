import random

dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]

dataset2 = [[2.0, 1.0, 0],
            [1.0, 3.0, 0],
            [2.0, 3.0, 0],
            [5.0, 3.0, 1],
            [7.0, 3.0, 1],
            [2.0, 4.0, 0],
            [3.0, 4.0, 0],
            [6.0, 4.0, 1],
            [1.0, 5.0, 0],
            [2.0, 5.0, 0],
            [5.0, 5.0, 1],
            [4.0, 6.0, 1],
            [6.0, 6.0, 1],
            [5.0, 7.0, 1]]


class Perceptron:
    bias = 0
    weights = []

    def __init__(self, activation_func):
        self.activation_func = activation_func

    def predict(self, row):
        activation = self.bias
        for i in range(len(row) - 1):
            activation += self.weights[i] * row[i]
        return self.activation_func(activation)

    def train(self, train_data, learning_rate, epoch_number):
        self.weights = [random.uniform(0, 1) for i in range(len(train_data[0])-1)]
        for epoch in range(epoch_number):
            sum_error = 0.0
            for row in train_data:
                prediction = self.predict(row)
                error = row[-1] - prediction
                sum_error += error*error
                self.bias = self.bias + learning_rate * error
                for i in range(len(row)-1):
                    self.weights[i] = self.weights[i] + learning_rate * error * row[i]
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, learning_rate, sum_error))


def jedenzero(a):
    if a >= 0:
        return 1
    else:
        return 0


p = Perceptron(jedenzero)
p.train(dataset2, 0.01, 20)
print(p.bias)
print(p.weights)
