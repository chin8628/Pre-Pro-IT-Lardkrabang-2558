""" W1_D4_Login """
def main(username, password):
    """ lfgodf """
    if (len(username) * 3) == len(password):
        print("User " + username + " Password "+ "*"*len(password) + "; Access granted!")
    else:
        print("User " + username + " Password " + "*"*len(password) + "; Access denied!")
main(input(), input())
