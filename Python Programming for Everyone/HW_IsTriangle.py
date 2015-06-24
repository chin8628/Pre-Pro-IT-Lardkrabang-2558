""" HW_IsTriangle """
def main():
    """ Poi kak """
    poi = []
    poi.append(int(input()))
    poi.append(int(input()))
    poi.append(int(input()))
    poi.sort()
    if poi[2]**2 == poi[0]**2 + poi[1]**2:
        print("Yes.")
    else:
        print("No.")
main()
