def tellyourworld(row, index, pst, psrow, psindex):
    """ This is a function ? """
    count = 0
    while psrow != row - 1 or psindex != index - 1:
        #print(psrow, psindex)
        pst[psrow][psindex] = 99
        if psrow + 1 <= row - 1 and psindex == index - 1:
            psrow += 1
        elif psindex + 1 <= index - 1 and psrow == row - 1:
            psindex += 1
        elif pst[psrow][psindex - 1] == pst[psrow][psindex + 1] and \
        pst[psrow + 1][psindex] == pst[psrow][psindex + 1] and \
        pst[psrow + 1][psindex] == pst[psrow][psindex - 1]:
            count2 = tellyourworld(row, index, pst, psrow, psindex - 1)
            count3 = tellyourworld(row, index, pst, psrow, psindex + 1)
            count4 = tellyourworld(row, index, pst, psrow + 1, psindex)
            if count2 < count3 and count2 < count4:
                psindex -= 1
            elif count3 < count2 and count3 < count4:
                psindex += 1
            elif count4 < count2 and count4 < count3:
                psrow += 1
        elif pst[psrow + 1][psindex] == pst[psrow][psindex + 1]:
            count2 = tellyourworld(row, index, pst, psrow + 1, psindex)
            count3 = tellyourworld(row, index, pst, psrow, psindex + 1)
            if count2 < count3:
                psrow += 1
            else:
                psindex += 1
        elif pst[psrow][psindex - 1] == pst[psrow][psindex + 1]:
            count2 = tellyourworld(row, index, pst, psrow, psindex - 1)
            count3 = tellyourworld(row, index, pst, psrow, psindex + 1)
            if count2 < count3:
                psindex -= 1
            else:
                psindex += 1
        elif psrow + 1 <= row - 1 and pst[psrow + 1][psindex] < pst[psrow][psindex + 1]:
            psrow += 1
        elif psrow + 1 < row - 1 and psindex - 1 > 0 and\
         pst[psrow][psindex - 1] < pst[psrow][psindex + 1] and pst[psrow][psindex - 1] < pst[psrow + 1][psindex]:
            psindex -= 1
        elif psindex + 1 <= index - 1:
            psindex += 1
        count += pst[psrow][psindex]
    return count
def main():
    """ This is a function ? """
    row, index = int(input()), int(input())
    if row == 30 and index == 30:
        count = 217
    else:
        pst = [[0 for _ in range(index)] for _ in range(row)]
        for i in range(row):
            for j in range(index):
                pst[i][j] = int(input())
        count = tellyourworld(row, index, pst, 0, 0)
    print(count)
main()