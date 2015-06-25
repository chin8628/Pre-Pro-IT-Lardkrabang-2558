""" W1_D3_ManU """
def main(cost):
    """ This is function """
    print(("%0.3f" % (cost-cost*[20, 18, 15, 10, 7][(cost <= 20)+(cost <= 30)+(cost <= 40)+ \
    (cost <= 60)]/100)) if cost >= 10 else ("I don't care."))
main(int(input()))
