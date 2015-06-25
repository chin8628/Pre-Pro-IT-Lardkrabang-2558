""" W1_D2_Compare """
def main(inputa, inputb):
    """ GG WP """
    print("A = B") if inputa == inputb else print(("A > B", "A < B")[inputa < inputb])
main(int(input()), int(input()))
