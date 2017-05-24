#S.McDonald 11/1/2016
#maximum_two_values
#This program finds the maximum of two numbers entered by the user


#input
def get_input():
    #prompt the user to enter the value
    value = int(input("Enter a value: "))
    return value


#processing
def find_max(val1, val2):
    #compare the two numbers and return the greater one
    if val1 > val2:
        print(val1, " is greater than ", val2)
        max1 = val1
    elif val1 == val2:
        print("Both numbers are equal to ", val1)
        max1 = val1
    else:
        print(val2, " is greater than ", val1)
        max1 = val2
    return max1 #return the greater value


def main():
    #get user's input for val1 and val2
    val1 = get_input()
    val2 = get_input()
    max1 = find_max(val1, val2)





#call main
main()


