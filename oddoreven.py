while 1:
    number=raw_input("please enter a number")
    number=int(number)
    if number%4 == 0:
        print("the number is the multiple of 4")
    if number%2 == 0:
        print("the number is even")
    else :
        print("the number is odd")
    reply=raw_input("Do you want to continue: Y/N")
    if reply == 'Y':
        continue
    else:
        break

