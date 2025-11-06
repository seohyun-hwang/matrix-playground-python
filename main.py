import numpy


matrices = []
matrixNames = []
matrixSizes = []

print("Hi. This program allows you to experiment calculations with square matrices.")
while True:
    userChoice = int(input("1: CREATE. 2: READ. 3: UPDATE. 4: DELETE. 5: OPERATE. 6: QUIT.\n"))
    if userChoice == 1:
        print("You chose CREATE.")
        matrixSizeInitial = int(input("Row/column count: "))
        if matrixSizeInitial == 0:
            print("Ain't no way you're making a matrix of size 0...")
        elif matrixSizeInitial > 0:
            matrixNames.append(input("Name of matrix: "))
            matrixSizes.append(matrixSizeInitial)
            list_rows = []
            for i in range(matrixSizeInitial):
                list_rowValues = []
                for j in range(matrixSizeInitial):
                    list_rowValues.append(float(input("Value at [row " + str(i + 1) + "][column " + str(j + 1) + "]: ")))
                list_rows.append(numpy.array(list_rowValues))
            matrices.append(numpy.array(list_rows))
        else:
            print("You messed up")
    elif userChoice == 2:
        print("You chose READ.")
        nameOf_selectedMatrix = input("Name of matrix: ")
        isMatrixFound = 0
        for a in range(len(matrixNames)):
            if matrixNames[a] == nameOf_selectedMatrix:
                isMatrixFound = 1
                print("Found! Name: " + nameOf_selectedMatrix)
                matrixSize = matrixSizes[a]
                for b in range(matrixSize):
                    print(matrices[a][b])
                #print("\nDeterminant: " + getDeterminant(matrices[a]))
        if isMatrixFound == 0:
            print("No matching matrix found!")
    elif userChoice == 3:
        print("You chose UPDATE.")
        nameOf_selectedMatrix = input("Name of matrix: ")
        isMatrixFound = 0
        for a in range(len(matrixNames)):
            if matrixNames[a] == nameOf_selectedMatrix:
                isMatrixFound = 1
                print("Found! Name: " + nameOf_selectedMatrix)
                while True:
                    updateRow = int(input("Row of update: "))
                    updateColumn = int(input("Column of update: "))
                    newValue = float(input("New value: "))
                    if 1 <= updateRow <= matrixSizes[a] and 1 <= updateColumn <= matrixSizes[a]:
                        matrices[a][updateRow - 1][updateColumn - 1] = newValue
                    else:
                        print("You messed up")
                    if input("More edits? (y/n) ") == "n":
                        break
        if isMatrixFound == 0:
            print("No matching matrix found!")
    elif userChoice == 4:
        print("You chose DELETE.")
        nameOf_selectedMatrix = input("Name of matrix: ")
        isMatrixFound = 0
        for a in range(len(matrixNames)):
            if matrixNames[a] == nameOf_selectedMatrix:
                isMatrixFound = 1
                print("Found! Name: " + nameOf_selectedMatrix)
                matrices.pop(a)
                matrixNames.pop(a)
                matrixSizes.pop(a)
        if isMatrixFound == 0:
            print("No matching matrix found!")
    elif userChoice == 5:
        print("You chose OPERATE.")

    elif userChoice == 6:
        print("You chose QUIT.")
        print("Goodbye. Closing program...")
        break
    else:
        print("You messed up")

#def getDeterminant(matrixIndex):