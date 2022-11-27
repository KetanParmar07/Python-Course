# string = string is a collection of character
# string represents in the single, double quotation symbol
# string is also represent in the triple quotation symbol
# every string character access using index value
# index value always start with 0 for left to right iteration and -1 for right to left iteration

# string example given below
string = 'Hello World'
string1 = "My name is  Ketan Parmar"
string2 = '''
            Good, Morning
            Hello, My name is ketan
            what are doing?
'''
print(string)
print(string1)
print(string2)

print(string[4])
print(string1[3])
print(string2[50])

# string slicing example
str = 'Good, Morning'
print(str[2])
print(str[0:7])
print(str[0:10:2])
print(str[-1:-10:-1])
print(str[-1::-1])