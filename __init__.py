import random
import timeit


def generateNumList(size, numrange):
    numList = random.sample(range(numrange), size)

    return numList


def searchLinear(x, numList, length):
    # n is the number of passes through the loop to find the number
    n = 0
    # print(x)
    # print(numList)
    for i in range(length):
        n = n + 1
        if numList[i] == x:
            return i, n
    return -1, n


def searchBinary(x, numList):
    # set low and high markers

    low = 0  # set initial low
    high = len(numList) - 1  # set initial high
    n = 0  # the number of halvings

    while low <= high:  # while there is still a range to search
        n = n + 1
        mid = (low + high) // 2  # position of middle item
        midItem = numList[mid]  # value of middle item
        if x == midItem:
            return mid, n  # found it!! return mid
        elif x < midItem:  # x is in lower half of the range
            high = mid - 1  # move high marker down
        else:
            # x > midItem, #x is in the higher half
            low = mid + 1  # move the low marker up

    return - 1, n  # -1, if x is not in the list


linearPassCount = 0
binaryPassCount = 0


def simSearch(searchType, numrange, simList, length):
    # searchType "linear" or "binary"
    global linearPassCount
    global binaryPassCount
    if searchType.lower() == "linear":
        position, passCount = searchLinear(random.randint(1, numrange), simList, length)
        linearPassCount = linearPassCount + passCount
    else:
        position, passCount = searchBinary(random.randint(1, numrange), simList)
        binaryPassCount = binaryPassCount + passCount

    return passCount


def main():
    global linearPassCount
    global binaryPassCount

    numrange = int(input("How many items in the list? "))
    # numsearch =input("How many searches would you like to run? ")
    numsearch = 1000
    searchList = generateNumList(numrange, numrange)
    searchSortList = sorted(generateNumList(numrange, numrange))

    # reset global counts
    linearPassCount = 0
    binaryPassCount = 0

    # print(searchList)
    # print(searchSortList)

    b = timeit.Timer('simSearch(\'binary\',' + str(numrange) + ',' + str(searchSortList) + ',0)',
                     "from __main__ import simSearch")
    l = timeit.Timer(
        'simSearch(\'linear\',' + str(numrange) + ',' + str(searchSortList) + ',' + str(len(searchList)) + ')',
        "from __main__ import simSearch")

    # b = timeit.Timer('simSearch(\'binary\')')

    bTotalTime = b.timeit(numsearch)
    lTotalTime = l.timeit(numsearch)
    bAvg = bTotalTime / numsearch
    lAvg = lTotalTime / numsearch
    bAvgPass = binaryPassCount / numsearch
    lAvgPass = linearPassCount / numsearch

    print("{0:12}{1:>10}{2:>15}{3:>25}{4:>30}".format("Search Type", "# Searches", "List Size", "Avg. Iterations",
                                                      "Average Time"))
    print("-" * 100)
    print("{0:12}{1:>10}{2:>15}{3:>25}{4:>30.20f}".format("Linear", numsearch, numrange, lAvgPass, lTotalTime, lAvg))
    print("{0:12}{1:>10}{2:>15}{3:>25}{4:>30.20f}".format("Binary", numsearch, numrange, bAvgPass, bTotalTime, bAvg))


if __name__ == "__main__":
    main()

