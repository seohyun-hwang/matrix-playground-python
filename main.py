import numpy


matrices = []
matrixNames = []
matrixSizes = []

print("Hi. This program allows you to experiment calculations with square matrices.")
while True:
    userChoice = int(input("1: CREATE. 2: READ. 3: UPDATE. 4: DELETE. 5: OPERATE. 6: FIND PROPERTY. 7: QUIT.\n"))
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
            print("You messed up. The answer should have been an integer greater than 0.")
    elif userChoice == 2:
        print("You chose READ.")
        nameOf_selectedMatrix = input("Name of matrix: ")
        isMatrixFound = 0
        for a in range(len(matrixNames)):
            if matrixNames[a] == nameOf_selectedMatrix:
                isMatrixFound = 1
                print("Found! Name: " + nameOf_selectedMatrix)
                for b in range(matrixSizes[a]): #matrixSizes[a] = size of selected matrix
                    print(matrices[a][b]) # printing each row of the selected matrix
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
                        print("You messed up. You're trying to access a row or column that is out of bounds.")
                    if input("More edits? (y/n) ") == "n":
                        break
        if isMatrixFound == 0:
            print("No matching matrix found!")
    elif userChoice == 4:
        print("You chose DELETE.")
        userChoice_selectedMatrix = input("Name of matrix: ")
        isMatrixFound = 0
        for a in range(len(matrixNames)):
            if matrixNames[a] == userChoice_selectedMatrix:
                isMatrixFound = 1
                print("Found! Name: " + userChoice_selectedMatrix)
                matrices.pop(a)
                matrixNames.pop(a)
                matrixSizes.pop(a)
        if isMatrixFound == 0:
            print("No matching matrix found!")
    elif userChoice == 5:
        print("You chose OPERATE.")
        userChoice_update = int(input("1: TRANSPOSE. 2: INVERT. 3: DOT PRODUCT. 4: CROSS PRODUCT. 5: MATRIX MULTIPLICATION. 6: MATRIX ADDITION"))
        if userChoice_update == 1:
            print("You chose TRANSPOSE.")
            userChoice_selectedMatrix = input("Name of matrix: ")
            isMatrixFound = 0
            for matrixNamesIndex in range(len(matrixNames)):
                if matrixNames[matrixNamesIndex] == userChoice_selectedMatrix:
                    isMatrixFound = 1
                    print("Found! Name: " + userChoice_selectedMatrix)
                    copiedMatrix = []
                    for a in range(matrixSizes[matrixNamesIndex]):
                        copiedMatrix.append([])
                        for b in range(matrixSizes[matrixNamesIndex]):
                            copiedMatrix[a].append(matrices[matrixNamesIndex][a][b])
                    for a in range(matrixSizes[matrixNamesIndex]):
                        for b in range(matrixSizes[matrixNamesIndex]):
                            matrices[matrixNamesIndex][a][b] = copiedMatrix[b][a]
                            copiedMatrix[a].append(matrices[matrixNamesIndex][a][b])
            if isMatrixFound == 0:
                print("No matching matrix found!")
            print("Transposition finished.")
        elif userChoice_update == 2:
            print("You chose INVERT.")
            userChoice_selectedMatrix = input("Name of matrix: ")

        elif userChoice_update == 3:
            print("You chose DOT PRODUCT.")
            userChoice_selectedMatrix = input("Name of matrix: ")

        elif userChoice_update == 4:
            print("You chose CROSS PRODUCT.")
            userChoice_selectedMatrix1 = input("Name of matrix 1: ")
            userChoice_selectedMatrix2 = input("Name of matrix 2: ")

        elif userChoice_update == 5:
            print("You chose MATRIX MULTIPLICATION.")
            userChoice_selectedMatrix = input("Name of matrix: ")

        elif userChoice_update == 6:
            print("You chose MATRIX ADDITION.")
            userChoice_selectedMatrix1 = input("Name of matrix 1: ")
            userChoice_selectedMatrix2 = input("Name of matrix 2: ")

        else:
            print("You messed up. The answer was supposed to be an integer between 1 and 6 inclusive.")
    elif userChoice == 6:
        print("You chose FIND PROPERTY.")
        userChoice_findProperty = int(input("1: DETERMINANT. 2: RANK. 3: NULL-SPACE. 4: LINEAR DEPENDENCE."))
    elif userChoice == 7:
        print("You chose QUIT.")
        print("Goodbye. Closing program...")
        break
    else:
        print("You messed up. You were supposed to answer with an integer between 1 and 7 inclusive.")