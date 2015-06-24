""" W1_D3_ManU """
def main(cost):
    """ This is function """
    if cost >= 61:
        print("%.3f" % float(cost - (cost*0.20)))
    elif cost >= 41:
        print("%.3f" % float(cost - (cost*0.18)))
    elif cost >= 31:
        print("%.3f" % float(cost - (cost*0.15)))
    elif cost >= 21:
        print("%.3f" % float(cost - (cost*0.10)))
    elif cost >= 10:
        print("%.3f" % float(cost - (cost*0.07)))
    else:
        print("I don't care.")
main(int(input()))
