a=10
b=100
print('The value of a is= ',a,'\nThe value of b is=',b)
print('The Memory Address value of a is= ',id(a),'\nThe Memory Address value of b is= ',id(b))
temp = a
a=b
b=temp
print('The value of a is= ',a,'\nThe value of b is=',b)
print('The Memory Address value of a is= ',id(a),'\nThe Memory Address value of b is= ',id(b))