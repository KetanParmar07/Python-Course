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
str1 = 'Good, Morning'
print(str1[2])
print(str1[0:7])
print(str1[0:10:2])
print(str1[-1:-10:-1])
print(str1[-1::-1])

# string iteration using loop
print('The string length is= ',len(string))

for i in range(len(string)):
    print(string[i])

print('------------------------------------------')

str1 = string[-1::-1]
for i in range(len(str1)):
    print(str1[i])

# or second method reverse iteration in string
for i in range(len(string)-1,-1,-1):
    print(string[i])

# different string in-built function given below
# 1) .lower() -> convert given string in lower-case letter
# 2) .upper() -> convert given string in upper-case letter
# 3) .title() -> convert given string all word first letter into upper-case letter
# 4) .capitalize() -> convert given string sentence only first letter in upper-case and all other word first letter in lower case format
# 5) .find() -> here find function return the search particular character index value and character is not found then return -1
# 6) .index() -> here index function return the index value for particular character or character is not found the get error
# 7) .isalpha() -> here isalpha function return the true or false value if given string in every character is alphabet then return true other wise return false value
# 8) .isdigit() -> here isdigit function return the true or false value if given string in every character is digit then return true other wise return false value
# 9) .isalnum() -> here isalnum function return the true or false value if given string in every character is alphabet or digit or number then return true other wise return false value
# 10) chr() -> here chr() function return the ASCII value to character
# 11) ord() -> here ord() function return the character to ASCII value
# 12) .format() -> here .format function use for when the program run that time in given string new string value add.
#                  and format value store in the {} -> (curly brackets) here line no. 69 in {>10} means right side of given new string                  range in 10 and {<10} means left side of given new string range in 10 and {^10} means middle part of given new string range in 10

print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())
print(string.find('e'))
print(string.index('o'))

str1 = 'welcome {f:<10} to {l:>10} new {m:^10}home'.format(f='Hello',l='our',m=10)
print(str1.isalpha())
print(str1.isalpha())
print(str1.isalnum())
print(str1)

x = chr(65)
print(x)
y = ord('A')
print(y)