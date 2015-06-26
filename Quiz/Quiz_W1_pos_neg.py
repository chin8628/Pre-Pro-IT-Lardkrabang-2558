""" Quiz_W1_pos_neg """
def main():
    """ This is a function """
    inputx = int(input())
    inputy = int(input())
    inputa = input()
    if inputa == "True":
        if (inputx < 0 and inputy >= 0) or (inputy < 0 and inputx >= 0):
            print("True")
        else:
            print("False")
    else:
        if (inputx >= 0 and inputy >= 0) or (inputx < 0 and inputy < 0):
            print("True")
        else:
            print("False")
main()
