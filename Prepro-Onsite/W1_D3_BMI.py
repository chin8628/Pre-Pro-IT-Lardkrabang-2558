""" W1_D3_BMI """
def main(weight, height):
    """ hahahahaha """
    bmi = float(weight/((height/100)**2))
    if bmi >= 30:
        print("Obese")
    elif 25 <= bmi:
        print("Overweight")
    elif 18.5 <= bmi:
        print("Normal")
    else:
        print("Underweight")

main(int(input()), int(input()))
