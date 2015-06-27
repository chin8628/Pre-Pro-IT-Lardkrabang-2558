""" W1_D4_CircleInRectangle """
def main(inputw, inputh, inputx, inputy, inputr):
    """ ALKFJLKASF """
    disx = inputr + inputx
    disy = inputr + inputy
    print(["Yes", "No"][disx > inputw or disx < 0 or disy > inputh or disy < 0])
main(int(input()), int(input()), int(input()), int(input()), int(input()))
