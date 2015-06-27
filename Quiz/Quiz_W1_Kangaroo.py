""" Quiz_W1_Kangaroo """
def main(inpa):
    """ So lazy """
    print([inpa[1] - inpa[0] - 1, inpa[2] - inpa[1] - 1][inpa[2] - inpa[1] > inpa[1] - inpa[0]])
main(sorted(map(int, [input(), input(), input()])))
