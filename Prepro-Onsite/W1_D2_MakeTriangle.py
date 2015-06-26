""" W1_D2_MakeTriangle """
def main(aaa):
    """ Notice me senpai """
    print(("NO", "YES")[max(aaa) <= sum(sorted(aaa)[:-1])])
main([int(input()), int(input()), int(input())])
