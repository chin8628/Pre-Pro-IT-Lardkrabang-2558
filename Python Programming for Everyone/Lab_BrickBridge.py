"""" Lab_BrickBridge """
def main():
    """ WOW DOUGE """
    smallblock = int(input())
    largeblock = int(input())
    tempsmallblock = smallblock
    goal = int(input())
    while goal > 0 and largeblock > 0:
        goal = goal - 5
        largeblock = largeblock - 1
    if largeblock <= 0 and goal < 0:
        goal = goal + 5
    while goal > 0 and smallblock > 0:
        goal = goal - 1
        smallblock = smallblock - 1
    if smallblock <= 0 and goal < 0:
        goal = goal + 1
    if goal == 0:
        print(tempsmallblock - smallblock)
    else:
        print("-1")
main()
