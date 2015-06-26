""" W1_D2_SumSumSum """
def main(inputa, inputb):
    """ HiHiHi """
    print(inputa * 2 + inputb * 2) if inputa == inputb else \
    print((inputa * 2 + inputb, inputa + inputb * 2)[inputa < inputb])
main(int(input()), int(input()))
