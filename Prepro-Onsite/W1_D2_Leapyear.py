""" W1_D2_Leapyear """
def main(yea):
    """ Thaiwitter """
    print(((yea%4 == 0 and yea % 100 != 0) or (yea % 400 == 0)))
main(int(input()) - 543)
