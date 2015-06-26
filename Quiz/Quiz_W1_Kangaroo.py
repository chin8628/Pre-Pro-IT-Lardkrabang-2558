""" Quiz_W1_Kangaroo """
def main():
    """ So lazy """
    inputa = [int(input()), int(input()), int(input())]
    inputa.sort()
    if inputa[2] - inputa[1] > inputa[1] - inputa[0]:
        print(inputa[2] - inputa[1] - 1)
    else:
        print(inputa[1] - inputa[0] - 1)
main()
