num1 = float(input('Enter Number1:- '))
num2 = float(input('Enter Number2:- '))
operator = input('Enter Mathematical Notation:- ')

if operator == '+':
    print('The Sum of two number = ',(num1+num2))
elif operator == '-':
    print('The Subtraction of two Number = ',(num1-num2))
elif operator == '*':
    print('The Multiplication of two Number = ',(num1*num2))
elif operator == '/':
    print('The Division of two Number = ',(num1/num2))
elif operator == '%':
    print('The Modulas of two Number = ',(num1%num2))
elif operator == '**':
    print('The Power of this Number = ',(num1**num2))
elif operator == '//':
    print('The Floor value is = ',(num1//num2))
else:
    print('Invalid Input...')