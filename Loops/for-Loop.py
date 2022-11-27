# range(5)
# here one parameter using for condition
# here for loop start value always 0
# for loop goes to 5-1 = 4
# and increment by always 1

# range(1,5)
# here two parameter using for loop first value for start condition and second value for condition check
# here for loop start value 1
# for loop goes to 5-1 = 4
# and increment by always 1

# range(1,5,2)
# here one parameter using for loop first value for start condition and second value for condition check and third value for incerment or decrement value
# here for loop start value 1
# for loop goes to 5-1 = 4
# and increment by always 2

# Example of for loop given below
print('The number from 0 to 10: ')
for num in range(11):
    print(num)

print('------------------------------------------')

print('The number from 1 to 10: ')
for num in range(1,11):
    print(num)

print('------------------------------------------')

print('The number from 1 to 10: ')
for num in range(1, 11,3):
    print(num)

print('------------------------------------------')


num = int(input('Enter Number which table you want:- '))
for n in range(1,11):
    print(num,' x ',n,' = ',num*n)