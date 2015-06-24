""" HW_ARobot """
def main(lap):
    """ This is function """
    battery = []
    for i in range(lap):
        voltagelap = int(input())
        voltage = int(input())
        battery.append(0)
        j = 0
        while j < voltagelap:
            battery[i] += [0, 1][int(input()) < voltage]
            j += 1
    for i in range(lap):
        print(battery[i])
main(int(input()))
