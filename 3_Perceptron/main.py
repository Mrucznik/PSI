from sklearn.linear_model import perceptron
from pandas import *

inputs = DataFrame({
          'A': [2, 1, 2, 5, 7, 2, 3, 6, 1, 2, 5, 4, 6, 5],
          'B': [2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7],
    'Targets': [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]
})

# Create the perceptron object (net)
net = perceptron.Perceptron(max_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)

# Train the perceptron object (net)
net.fit(inputs[['A', 'B']], inputs['Targets'])

# Output the coefficints
print("Coefficient 0 " + str(net.coef_[0, 0]))
print("Coefficient 1 " + str(net.coef_[0, 1]))
print("Bias " + str(net.intercept_))


