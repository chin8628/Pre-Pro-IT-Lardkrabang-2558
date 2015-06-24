""" HW_Robot1 """
import math
def main():
    """ dfjk """
    name = str(input())
    year = math.floor(float(input()))
    print([str(name) + ", you shall not pass.", str(name) + ", you can pass."][year < 18])
main()
