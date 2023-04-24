#Taking the single input from command line input.

#Intefer
int_a = int(input('Enter an integer value: '))

#Decimal/Floating
float_a = float(input('Enter a floating/decimal value: '))

#Character/String
str_a = input('Enter Character or String: ')


if __name__ == "__main__":
    print('Interger: {0}\nDecimal: {1}\nCharacter/String: {2}'.format(int_a, float_a, str_a))
