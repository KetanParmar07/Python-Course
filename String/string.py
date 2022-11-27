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

# string iteration using loop
print('The string length is= ',len(string))

for i in range(len(string)):
    print(string[i])

print('------------------------------------------')

str = string[-1::-1]
for i in range(len(str)):
    print(str[i])

# or second method reverse iteration in string
for i in range(len(string)-1,-1,-1):
    print(string[i])

# different string in-built function given below
# 1) .lower() -> convert given string in lower-case letter
# 2) .upper() -> convert given string in upper-case letter
# 3) .title() -> convert given string all word first letter into upper-case letter
# 4) .capitalize() -> convert given string sentence only first letter in upper-case and all other word first letter in lower case format
# 5) .find() -> here find function return the search particular character index value
# 6) .index() ->
# 7) .isalpha() ->
# 8) .isdigit() ->
# 9) .isalnum() ->

print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())
print(string.find('e'))