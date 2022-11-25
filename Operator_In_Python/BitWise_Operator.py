x=int(input('Enter number: '))
y=int(input('Enter number: '))

#  Bitwise & operator
print('The Binary value of x is= ',bin(x))
print('The Binary value of y is= ',bin(y))

# x = 10 -> Binary = 1010
# y = 8  -> Binary = 1000
# x&y =  -> Binary = 1000 == 8(Decimal)
print('The Decimal value of Bitwise & operator is= ',x&y,'The Binary value of Bitwise & operator is= ', bin(x&y))

# x = 10 -> Binary = 1010
# y = 8  -> Binary = 1000
# x|y =  -> Binary = 1010 == 10(Decimal)
print('The Decimal value of Bitwise | operator is= ',x|y,'The Binary value of Bitwise | operator is= ', bin(x|y))

# x = 10 -> Binary = 1010
# y = 8  -> Binary = 1000
# x^y =  -> Binary = 0010 == 2(Decimal)
print('The Decimal value of Bitwise ^ operator is= ',x^y,'The Binary value of Bitwise ^ operator is= ', bin(x^y))
