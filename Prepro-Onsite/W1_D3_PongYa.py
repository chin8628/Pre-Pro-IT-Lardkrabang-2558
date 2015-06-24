""" W1_D3_PongYa """
def main(number):
    """ TEST """
    print([number, "PONG"][number % 3 == 0 or number % 10 == 3])
main(int(input()))
