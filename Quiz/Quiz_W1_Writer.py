""" Quiz_W1_Writer """
def main():
    """ WOW Bitcoin """
    inputstring = str(input())
    cost = 0
    if len(inputstring) <= 10:
        cost = 0
    elif len(inputstring) <= 30:
        cost = len(inputstring) * 1.23
    elif len(inputstring) <= 50:
        cost = len(inputstring) * 4.56
    else:
        cost = len(inputstring) * 9.99
    print("Pr!ze:=> %.4f bath" % cost)
main()
