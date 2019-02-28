

def relationScore(a, b):
    inAnotB = 0
    inBnotA = 0
    inBoth = 0
    for item in a:
        if item in b:
            inBoth+=1
        else:
            inAnotB+=1
    for item in b:
        if item not in a:
            inBnotA+=1
    return min(inBnotA, inBnotA, inBoth)


"""

"""
def getLines(lineListh, lineListv):
    for i in range(lineListv):
        matchLocation = i
        bestMatch = -1
        if lineListv[i] == False:
            continue
        for k in range(i+1, lineListv):
            if lineListv[k] == False:
                continue
            if relationScore(lineListv[i][2],lineListv[k][2])>bestMatch:
                bestMatch = relationScore(lineListv[i][2],lineListv[k][2])
                matchLocation = k
        lineListv[i][2] = lineListv[i][2].union(lineListv[matchLocation][2])
        lineListv[i][0] = lineListv[i][0] + " "+lineListv[k][0]
        lineListv[i][1] = lineListv[i][1] + lineListv[k][1]
        lineListv[k] = False
    newList = []
    for i in range(lineListv):
        if lineListv[i] != False:
            newList.append(lineListv[i])
    lineListv = newList
    almostOutput = []


    for data in lineListv:
        bestMatch = -1
        matchLocation = -1  ##check
        for k in range(lineListh):
            matchLocation = k
            if lineListv[k] == False:
                continue
            if relationScore(data[2],lineListv[k][2]) > bestMatch:
                bestMatch = relationScore(data[2], lineListv[k][2])
                matchLocation = k
        almostOutput.append(data)
        almostOutput.append(lineListv[matchLocation])
        lineListv[k] = False

    return almostOutput




