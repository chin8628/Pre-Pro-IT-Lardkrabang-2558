""" W1_D3_BMI """
def main(bmi):
    """ hahahahaha """
    print(("Underweight", "Normal", "Overweight", "Obese")[(bmi > 18.5) + (bmi > 25) + (bmi >= 30)])
main(float(int(input()) / ((int(input()) / 100) ** 2)))
