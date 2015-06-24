""" W1_D2_SumSumSum """
def main():
    """ HiHiHi """
    inputa = int(input())
    inputb = int(input())
    if inputa > inputb:
        inputa *= 2
    elif inputb > inputa:
        inputb *= 2
    else:
        inputa *= 2
        inputb *= 2
    print(inputa+inputb)
main()
