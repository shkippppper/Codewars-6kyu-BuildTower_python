
def tower_builder(n_floors):
    firstFloor = 1
    length = int(2*n_floors-1)
    finalResult = 0
    resultToPrint = []
    for x in range(n_floors):
        spaceBetweeen = int((length - firstFloor)/2)
        finalResult = " "*spaceBetweeen + "*"*firstFloor + " "*spaceBetweeen
        firstFloor = firstFloor+2
        resultToPrint.append(finalResult)
    return resultToPrint
