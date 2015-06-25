""" W1_D4_BookPrice """
def main(bookn, price, dis, moneysend, addition):
    """ WOW OWO SO WOW """
    sumn = (price - (price * (dis / 100))) * bookn
    print("%.1f" % float(sumn + moneysend + (addition * (bookn - 1))))
main(float(input()), float(input()), float(input()), float(input()), float(input()))
