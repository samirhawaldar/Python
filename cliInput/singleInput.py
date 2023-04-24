#Taking the single input from command line input.

def Display(loc_a):
    print("You Enterned: ", loc_a, "\n")

#Intefer
int_a = int(input('Enter an integer value: '))
Display(int_a)


#Decimal/Floating
float_a = float(input('Enter a floating/decimal value: '))
Display(float_a)


#Character/String
str_a = input('Enter Character or String: ')
Display(str_a)


#List with same data type.
list_int = list(map(int, input("Enter Interger list: ").split()))
print('Your list: ', list_int, "\n")


#List with Dissimilar Data
#Note: Data will be stored as a string in list.
list_dis = list(input("Enter any data: ").split())
print('You Dissimilar Data List: ',list_dis, "\n")


#Set with Dissimilar Data
#Note: Set holds unique values.
set_dis = set(input("Enter any data: ").split())
print('You Set Data: ',set_dis, "\n Duplicate entries will not be considered. Set holds uniques entries. Sets cannot be indexed.", '\n')


#Tuple
tup_a = tuple(input('Enter data for Tuple: ').split())
print('You Tuple Data: ',tup_a, "\nEnterned data cannot be changed. Tuple is mutable.", '\n')



if __name__ == "__main__":
    pass
