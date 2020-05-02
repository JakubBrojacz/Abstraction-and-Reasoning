import element


SPLITTING_TYPES = 6

def get_elements(matrix,
                 backgroundColor=0,
                 numberOfColors=10,
                 transparentColor=10):
    divisions = []
    divisions.append(everything_as_one_element(
        matrix, 0, 10))
    divisions.append(split_only_by_color(
        matrix, backgroundColor, transparentColor, numberOfColors))
    divisions.append(split(matrix, backgroundColor,
                           transparentColor, 4, True))
    divisions.append(split(matrix, backgroundColor,
                           transparentColor, 8, True))
    divisions.append(split(matrix, backgroundColor,
                           transparentColor, 4, False))
    divisions.append(split(matrix, backgroundColor,
                           transparentColor, 8, False))
    return divisions

def everything_as_one_element(matrix, 
                              backgroundColor,
                              transparentColor):
    listOfElements = []
    width = len(matrix[0])
    height = len(matrix)
    leftUpCornerElementFrame = (height, width)
    rightDownCornerOfElementFrame = (-1, -1)
    for row in range(height):
        for col in range(width):
            if matrix[row][col] != backgroundColor:
                if row > rightDownCornerOfElementFrame[0]:
                    rightDownCornerOfElementFrame = (
                        row, rightDownCornerOfElementFrame[1])
                if col > rightDownCornerOfElementFrame[1]:
                    rightDownCornerOfElementFrame = (
                        rightDownCornerOfElementFrame[0], col)
                if row < leftUpCornerElementFrame[0]:
                    leftUpCornerElementFrame = (
                        row, leftUpCornerElementFrame[1])
                if col < leftUpCornerElementFrame[1]:
                    leftUpCornerElementFrame = (
                        leftUpCornerElementFrame[0], col)
    
    elementFrameWidth = rightDownCornerOfElementFrame[1] - \
        leftUpCornerElementFrame[1] + 1
    elementFrameHeight = rightDownCornerOfElementFrame[0] - \
        leftUpCornerElementFrame[0] + 1
    matrixForElement = [[transparentColor for j in range(
        elementFrameWidth)] for k in range(elementFrameHeight)]
    for row in range(height):
        for col in range(width):
            if matrix[row][col] != backgroundColor:
                pos = (row - leftUpCornerElementFrame[0],
                       col - leftUpCornerElementFrame[1])
                matrixForElement[pos[0]][pos[1]] = matrix[row][col]
    el = element.Element(matrixForElement, leftUpCornerElementFrame, None)
    if el.width == 0:
        return []
    return [el]

def split_only_by_color(matrix,
                        backgroundColor,
                        transparentColor,
                        numberOfColors):
   
    listOfElements = []
    isColor = [False for i in range(numberOfColors)]
    leftUpCornerElementFrame = []
    rightDownCornerOfElementFrame = []
    width = len(matrix[0])
    height = len(matrix)
    
    for i in range(numberOfColors):
        leftUpCornerElementFrame.append((height, width))
        rightDownCornerOfElementFrame.append((-1, -1))

    for row in range(height):
        for col in range(width):
            currentColor = matrix[row][col]
            isColor[currentColor] = True
            if row > rightDownCornerOfElementFrame[currentColor][0]:
                rightDownCornerOfElementFrame[currentColor] = (
                    row, rightDownCornerOfElementFrame[currentColor][1])
            if col > rightDownCornerOfElementFrame[currentColor][1]:
                rightDownCornerOfElementFrame[currentColor] = (
                    rightDownCornerOfElementFrame[currentColor][0], col)
            if row < leftUpCornerElementFrame[currentColor][0]:
                leftUpCornerElementFrame[currentColor] = (
                    row, leftUpCornerElementFrame[currentColor][1])
            if col < leftUpCornerElementFrame[currentColor][1]:
                leftUpCornerElementFrame[currentColor] = (
                    leftUpCornerElementFrame[currentColor][0], col)

    matrices = []
    for i in range(numberOfColors):
        if isColor[i]:
            elementFrameWidth = rightDownCornerOfElementFrame[i][1] - \
                leftUpCornerElementFrame[i][1] + 1
            elementFrameHeight = rightDownCornerOfElementFrame[i][0] - \
                leftUpCornerElementFrame[i][0] + 1
            matrixForElement = [[transparentColor for j in range(
                elementFrameWidth)] for k in range(elementFrameHeight)]
            matrices.append(matrixForElement)
        else:
            matrices.append([None])

    for row in range(height):
        for col in range(width):
            currentColor = matrix[row][col]
            pos = (row - leftUpCornerElementFrame[currentColor][0],
                   col - leftUpCornerElementFrame[currentColor][1])
            matrices[currentColor][pos[0]][pos[1]] = currentColor

    for i in range(numberOfColors):
        if i != backgroundColor and isColor[i]:
            listOfElements.append(
                element.Element(matrices[i], leftUpCornerElementFrame[i], i))

    return listOfElements


def split(matrix, backgroundColor, transparentColor,
          spaceConnectionType=4, colorMatters=True):

    if spaceConnectionType not in [4, 8]:
        raise ValueError("spaceConnectionType should be 4 or 8")

    width = len(matrix[0])
    height = len(matrix)

    # isCellAssignedToSomeElement  = [[False] * width] * height

    isCellAssignedToSomeElement = [[False] * width for i in range(height)]

    stack = []
    listOfElements = []
    listOfCellsBelongingToElement = []
    for i in range(height):
        for j in range(width):
            if not isCellAssignedToSomeElement[i][j] and matrix[i][j] != backgroundColor:  # noqa
                stack.append((i, j))
                currentColor = matrix[i][j]
                rightDownCornerOfElementFrame = (i, j)
                leftUpCornerElementFrame = (i, j)
                listOfCellsBelongingToElement.clear()
                while len(stack) > 0:
                    currentCell = stack.pop()
                    col = currentCell[1]
                    row = currentCell[0]
                    isCellAssignedToSomeElement[row][col] = True
                    listOfCellsBelongingToElement.append(currentCell)

                    if row > rightDownCornerOfElementFrame[0]:
                        rightDownCornerOfElementFrame = (
                            row, rightDownCornerOfElementFrame[1])
                    if col > rightDownCornerOfElementFrame[1]:
                        rightDownCornerOfElementFrame = (
                            rightDownCornerOfElementFrame[0], col)
                    if row < leftUpCornerElementFrame[0]:
                        leftUpCornerElementFrame = (
                            row, leftUpCornerElementFrame[1])
                    if col < leftUpCornerElementFrame[1]:
                        leftUpCornerElementFrame = (
                            leftUpCornerElementFrame[0], col)

                    if colorMatters:
                        check_neighbours_color_matters(
                            matrix,
                            isCellAssignedToSomeElement,
                            stack,
                            currentColor,
                            row, col,
                            height, width,
                            spaceConnectionType)
                    else:
                        check_neighbours_color_not_matters(
                            matrix,
                            isCellAssignedToSomeElement,
                            stack,
                            backgroundColor,
                            row, col,
                            height, width,
                            spaceConnectionType)
                elementFrameWidth = rightDownCornerOfElementFrame[1] - \
                    leftUpCornerElementFrame[1] + 1
                elementFrameHeight = rightDownCornerOfElementFrame[0] - \
                    leftUpCornerElementFrame[0] + 1
                elementMatrix = [
                    [transparentColor] * elementFrameWidth
                    for k in range(elementFrameHeight)]
                for cell in listOfCellsBelongingToElement:
                    pos = (cell[0] - leftUpCornerElementFrame[0],
                           cell[1] - leftUpCornerElementFrame[1])
                    elementMatrix[pos[0]][pos[1]] = matrix[cell[0]][cell[1]]
                if colorMatters:
                    colorOfElement = currentColor
                else:
                    colorOfElement = None
                listOfElements.append(
                    element.Element(elementMatrix, leftUpCornerElementFrame,
                                    colorOfElement))

    return listOfElements


def check_neighbours_color_matters(matrix, isCellAssignedToSomeElement, stack,
                                   currentColor, row, col, height, width,
                                   spaceConnectionType):

    if (row > 0 and
        not isCellAssignedToSomeElement[row - 1][col] and
            matrix[row - 1][col] == currentColor):
        # up
        stack.append((row - 1, col))

    if (col > 0 and
        not isCellAssignedToSomeElement[row][col - 1]
            and matrix[row][col - 1] == currentColor):
        # left
        stack.append((row, col - 1))

    if (row < (height - 1) and
        not isCellAssignedToSomeElement[row + 1][col] and
            matrix[row + 1][col] == currentColor):
        # down
        stack.append((row + 1, col))

    if (col < (width - 1) and
        not isCellAssignedToSomeElement[row][col + 1] and
            matrix[row][col + 1] == currentColor):
        # right
        stack.append((row, col + 1))

    if spaceConnectionType == 8:
        if (row > 0 and col > 0 and
            not isCellAssignedToSomeElement[row - 1][col - 1] and
                matrix[row - 1][col - 1] == currentColor):
            # up-left
            stack.append((row - 1, col - 1))

        if (row > 0 and
            col < (width - 1) and
            not isCellAssignedToSomeElement[row - 1][col + 1] and
                matrix[row - 1][col + 1] == currentColor):
            # up-right
            stack.append((row - 1, col + 1))

        if (row < (height - 1) and
            col < (width - 1) and
            not isCellAssignedToSomeElement[row + 1][col + 1] and
                matrix[row + 1][col + 1] == currentColor):
            # down-right
            stack.append((row + 1, col + 1))

        if (row < (height - 1)
            and col > 0 and
            not isCellAssignedToSomeElement[row + 1][col - 1] and
                matrix[row + 1][col - 1] == currentColor):
            # down-left
            stack.append((row + 1, col - 1))


def check_neighbours_color_not_matters(matrix, isCellAssignedToSomeElement,
                                       stack, backgroundColor, row, col,
                                       height, width, spaceConnectionType):

    if (row > 0 and
        not isCellAssignedToSomeElement[row - 1][col] and
            matrix[row - 1][col] != backgroundColor):
        # up
        stack.append((row - 1, col))

    if (col > 0 and
        not isCellAssignedToSomeElement[row][col - 1] and
            matrix[row][col - 1] != backgroundColor):
        # left
        stack.append((row, col - 1))

    if (row < (height - 1) and
        not isCellAssignedToSomeElement[row + 1][col] and
            matrix[row + 1][col] != backgroundColor):
        # down
        stack.append((row + 1, col))

    if (col < (width - 1) and
        not isCellAssignedToSomeElement[row][col + 1] and
            matrix[row][col + 1] != backgroundColor):
        # right
        stack.append((row, col + 1))

    if spaceConnectionType == 8:
        if (row > 0 and
            col > 0 and
            not isCellAssignedToSomeElement[row - 1][col - 1] and
                matrix[row - 1][col - 1] != backgroundColor):
            # up-left
            stack.append((row - 1, col - 1))

        if (row > 0 and
            col < (width - 1) and
            not isCellAssignedToSomeElement[row - 1][col + 1] and
                matrix[row - 1][col + 1] != backgroundColor):
            # up-right
            stack.append((row - 1, col + 1))

        if (row < (height - 1) and
            col < (width - 1) and
            not isCellAssignedToSomeElement[row + 1][col + 1]
                and matrix[row + 1][col + 1] != backgroundColor):
            # down-right
            stack.append((row + 1, col + 1))

        if (row < (height - 1) and
            col > 0 and
            not isCellAssignedToSomeElement[row + 1][col - 1] and
                matrix[row + 1][col - 1] != backgroundColor):
            # down-left
            stack.append((row + 1, col - 1))
