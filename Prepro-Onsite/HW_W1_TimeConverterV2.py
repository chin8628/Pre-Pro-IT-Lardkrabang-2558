""" HW_W1_TimeConverterV2 """
def main(inputhr, inputmin):
    """ this is function """
    print("%02d:%02d %s" % (inputhr % 12, inputmin, ["AM", "PM"][inputhr > 12]))
main(int(input()), int(input()))
