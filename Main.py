# Created by Karim Zaher

# ///// Imports and Functions/////
import numpy as np

# ///// Editable Variables /////
iteration = 10000   # How many times gradient descent should run
learningRate = 0.005  # Learning rate used in gradient descent equation [See reference for Gradient Descent Equation]

# ///// Initialize variables and assign theta parameters /////
X = []
y = []
theta = [[0],   # Theta parameters will be used for our hypothesis equation [See reference for Hypothesis Equation]
         [0]]


# ///// Loop appends given co-ordinates to X and y array /////
givenInput = ''
numCoordPoints = 0
while True:
    givenInput = input("Input 'q' to quit.\nEnter a co-ordinate point in the following format\nX,y\n")
    if givenInput.lower() == 'q':
        break
    coordinate = givenInput.split(',')
    X.append([float(coordinate[0])])
    y.append([float(coordinate[1])])
    numCoordPoints += 1

# ///// Convert Python arrays to NumPy arrays /////
X = np.array(X)
y = np.array(y)
theta = np.array(theta)

X = np.insert(X, 0, 1, axis=1)  # Adds bias feature to X array
xTrans = X.transpose()

# ///// Gradient Descent /////
for i in range(0, iteration):
    hypothesis = np.dot(X, theta)
    difference = hypothesis - y
    cost = np.sum(difference ** 2) / (2 * numCoordPoints)   # Calculates the Cost Function
    print("Iteration %d | Cost: %f" % (i, cost))
    if cost == 0:
        break
    gradient = np.dot(xTrans, difference) / numCoordPoints  # Derivative of the Cost Function
    theta = theta - learningRate * gradient
    print(theta)

print("\nThe equation is:", str(float(theta[1])) + "X + " + str(float(theta[0])))