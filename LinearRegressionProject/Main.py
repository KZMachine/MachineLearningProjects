# Created by Karim Zaher

# ///// Imports and Functions/////
import numpy as np
import FileNamer
filenamer = FileNamer.SetFileName()

def fileCoords():
    X = []
    y = []
    numCoordPoints = 0
    filenamer.fileNamer()

    fileName = filenamer.getFileName()
    extension = filenamer.getExtension()
    file = open(fileName + ".csv",'r')
    xColumn = int(input("Which column are your X values in? [Column 1 -- Final Column]"))
    yColumn = int(input("Which column are your Y values in? [Column 1 -- Final Column]"))
    for line in file:
        data = line.split(',')

        try:    # Checks whether the coordinates are a numerical value or not
            tester = float(data[xColumn -1]) - 1
            tester = float(data[yColumn - 1]) - 1
            X.append([float(data[xColumn - 1])])
            y.append([float(data[yColumn - 1])])
            numCoordPoints += 1
        except:     # If the coordinates are not numerical, it continues to the next coordinate
            continue
    file.close()
    print(X)
    return [X, y, numCoordPoints]


def typeCoords():
    """Function runs if the user decides to manually type co-ordinate points"""
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
    return [X, y, numCoordPoints]

# ///// Editable Variables /////
iteration = 10000   # How many times gradient descent should run
learningRate = 0.005  # Learning rate used in gradient descent equation [See reference for Gradient Descent Equation]

# ///// Initialize variables and assign theta parameters /////
X = []
y = []
theta = [[0],   # Theta parameters will be used for our hypothesis equation [See reference for Hypothesis Equation]
         [0]]


# ///// Loop appends given co-ordinates to X and y array /////
choice = 100

while choice not in [1,2]:
    print("How would you like to input dataset?")
    print("1- Provide co-ordinate points using a .csv file\n2- Type co-ordinate points")
    try:
        choice = int(input("Enter a numerical value: "))
        if choice not in [1,2]:
            print("--" * 5)
            print("That choice is not an option.")
    except ValueError:
        print("--" * 5)
        print("Invalid input")
    print("--" * 5)

if choice == 1:
    X, y, numCoordPoints = fileCoords()
if choice == 2:
    X, y, numCoordPoints = typeCoords()


# ///// Convert Python arrays to NumPy arrays /////
X = np.array(X)
y = np.array(y)
theta = np.array(theta)

X = np.insert(X, 0, 1, axis=1)  # Adds bias feature to X array
xTrans = X.transpose()
print("Test2")
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