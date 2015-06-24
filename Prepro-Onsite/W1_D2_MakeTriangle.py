""" W1_D2_MakeTriangle """
def main():
    """ Notice me senpai """
    input1 = int(input())
    input2 = int(input())
    input3 = int(input())

    if input1 > input2+input3 or input2 > input1+input3 or input3 > input2+input1:
        print("NO")
    else:
        print("YES")
main()
