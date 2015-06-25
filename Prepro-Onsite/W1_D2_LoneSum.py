""" W1_D2_LoneSum """
def main(aaa):
    """ def top """
    print(sum([i for i in aaa if aaa.count(i) < 2]))
main([int(input()), int(input()), int(input())])
