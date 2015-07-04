""" HW_W2_HaPaSi """
def main():
    """ ZZzz """
    count = 0
    scorea, scoreb, draw = 0, 0, 0
    while scoreb < 5 and scorea < 5 and draw != 5:
        inputn = input()
        count += 1
        if inputn[0] == inputn[4]:
            draw += 1
        else:
            draw = 0
            if inputn[0] == 'H' and inputn[4] == 'S':
                scorea += 1
            elif inputn[0] == 'P' and inputn[4] == 'H':
                scorea += 1
            elif inputn[0] == 'S' and inputn[4] == 'P':
                scorea += 1
            elif inputn[4] == 'H' and inputn[0] == 'S':
                scoreb += 1
            elif inputn[4] == 'P' and inputn[0] == 'H':
                scoreb += 1
            elif inputn[4] == 'S' and inputn[0] == 'P':
                scoreb += 1
    if draw == 5:
        print("NONE")
    elif scorea == 5:
        print("A")
    elif scoreb == 5:
        print("B")
    print(count)
main()
