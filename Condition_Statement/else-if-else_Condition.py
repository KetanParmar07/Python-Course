Marks = int(input('Enter a value:- '))

# if statement
# if statement syntax:-
# if condition(True):
        # body
# elif condition(True):
        # body
# else:
        # body

if Marks > 90:
    print( 'A Grade')
elif Marks > 80 and Marks <= 90:
    print('B Grade')
elif Marks > 70 and Marks <= 80:
    print('C Grade')
elif Marks > 60 and Marks <= 70:
    print('D Grade')
elif Marks > 50 and Marks <= 60:
    print('E Grade')
elif Marks > 40 and Marks <= 50:
    print('F Grade')
else:
    print('you are Fail...')