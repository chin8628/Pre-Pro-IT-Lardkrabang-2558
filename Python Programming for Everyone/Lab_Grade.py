""" Lab_Grade """
def main():
    """ WAttt """
    inputgrade = int(input())
    if inputgrade >= 100:
        print("A", end="")
    elif inputgrade >= 90:
        print("B", end="")
    elif inputgrade >= 80:
        print("C", end="")
    elif inputgrade >= 70:
        print("D", end="")
    else:
        print("F", end="")
    if (inputgrade % 10) >= 5 and inputgrade < 100 and inputgrade >= 70:
        print("+")

main()
