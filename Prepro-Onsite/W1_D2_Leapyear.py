""" W1_D2_Leapyear """
any(filter(lambda x: print(x%4 == 0 and x%100 != 0 or x%400 == 0), [int(input())-543]))
