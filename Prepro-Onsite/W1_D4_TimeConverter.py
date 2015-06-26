""" W1_D4_TimeConverter """
def main(second):
    """ falfdsldslafklsakl """
    hour = str(int(second / 3600))
    second = second % 3600
    minute = str(int(second / 60))
    second = str(second % 60)
    print(hour + " hours, " + minute + " minutes, " + second + " seconds.")
main(int(input()))
