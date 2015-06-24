""" W1_D3_Salary """
def main(salary, addition):
    """ this is function """
    if salary >= 50000.01:
        addition = 0.04
    elif salary >= 25000.01:
        addition = 0.07
    elif salary >= 15000.01:
        addition = 0.10
    elif salary >= 7000.01:
        addition = 0.12
    else:
        addition = 0.15
    print("%.2f" % float(salary + (salary * addition)))
    print("%.2f" % float(salary * addition))
    print(str(int(addition * 100)) + "%")
main(float(input()), 0)
