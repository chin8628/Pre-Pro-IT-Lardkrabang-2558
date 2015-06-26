""" W1_D4_Luck_sum """
def main(inputn, sumn=0):
    """ WOW """
    for i in inputn:
        if i == 13:
            break
        else:
            sumn += i
    print(sumn)
main(inputn=[int(input()), int(input()), int(input())])
