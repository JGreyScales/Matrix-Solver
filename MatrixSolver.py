Matrixes = [[3, 5, 7, -2, -3, -2, -1],
            [12, 0, 7, 5, -5, 4, 2],
            [-2, 2, 0, 6, 3, -9, 4],
            [2, -1, 0, -12, 2, 1, -7],
            [1, -1, 1, 1, 1, -1, -7],
            [2, 2, 10, 2, -1, 15, 2]]
alphabet = ["x","y","z","w","v","k"]
planesToIgnore = []

# if row[RowNum] = 0, then swap rows with one in which that position is not equal to 0 and recalculate the constant
for rowID, row in enumerate(Matrixes):
     if row[rowID] == 0:
          for rowID2, row2 in enumerate(Matrixes):
               if (row2[rowID] != 0) and (row[rowID2] != 0):
                    Matrixes[rowID], Matrixes[rowID2] = Matrixes[rowID2], Matrixes[rowID]
                    break
            
print(*Matrixes, sep="\n")
# Iterate over all spots by going from column to column
for rowNum, row in enumerate(Matrixes):

    if rowNum in planesToIgnore: continue

    # We want our row[RowNum] to equal 1 when divided by itself
    divisor = row[rowNum]
    for columnPos in range(len(row[rowNum::])):
        Matrixes[rowNum][columnPos + rowNum] /= divisor

    for height in range(len(row) - 1):
        if height in planesToIgnore: continue
        # Ignore current spot
        if rowNum == height: continue

        constant = Matrixes[height][rowNum] / row[rowNum]

        for columnPos in range(len(row[rowNum::])):
                    Matrixes[height][columnPos + rowNum] -= constant * Matrixes[rowNum][columnPos + rowNum]
    
    # Check if any rows are equal to each other
    for id, plane in enumerate(Matrixes[:-1]):
          for id2, plane2 in enumerate(Matrixes):
                if (id == id2) or (id in planesToIgnore) or (id2 in planesToIgnore): continue
                elif plane == plane2:
                    planesToIgnore.append(id2)

    


match len(planesToIgnore):
    case 0:
        for rowID, row in enumerate(Matrixes):
            print(f"{alphabet[rowID]} = {row[-1]}")
    case 1:
        for rowID, row in enumerate(Matrixes):
            if rowID in planesToIgnore: print(f"{alphabet[rowID]} = T")
            else:
                for num in row[:-1]:
                    if 0 != num != 1:
                        print(f"{alphabet[rowID]} = {row[-1]} - {num}T")
                        break
    case _:
          print(*Matrixes, sep="\n")

exit(1)
