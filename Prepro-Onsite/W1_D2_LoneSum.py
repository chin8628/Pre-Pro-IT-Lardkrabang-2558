""" W1_D2_LoneSum """
def main():
    """ def top """
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    answer = 0
    if aaa != bbb and aaa != ccc:
        answer += aaa
    if bbb != aaa and bbb != ccc:
        answer += bbb
    if ccc != aaa and ccc != bbb:
        answer += ccc
    print(answer)

main()