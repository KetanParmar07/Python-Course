x = 10
y = 7.333
z = 1+2j

# int
# integer is immutable data-type it can't be modifide
print(x,' is Data-Type equal to ',type(x))

# float
# float is immutable data-type it can't be modifide
print(y,' is Data-Type equal to ',type(y))

# complex number
# complex number is immutable data-type it can't be modifide
print(z,' is Data-Type equal to', type(z))

# string
# string is immutable data-type it can't be modifide
s = 'ketan'
print(s,type(s))
s = '''
        Good, Morning
        Hello, My name is ketan
        what are doing?
    '''
print(s,type(s))

# List Data-Type
# List is mutable data-type
# List is slower than the Tuple data-type
l = [1,'ketan',4.768786,[2,46,75],(55,433,1+3j)]
print(l,type(l))
l[3][0] = [11,22,33,44]
print(l,type(l))

# Tuple Data-Type
t = (11,2,'hello',2+3j,'hgjjj')
print(t,type(t))
# t[0] = 'ketan' here tuple data-type is not mutable data-type so it can't be update the tuple value
#  and tuple data-type is  faster than list data-type

# Dictionary Data-Type
# Dictionary is mutable data-type
d = {
    'course_name': "python",
    'course_duration': '3 months'
}
print(d,type(d))
d['course_duration'] = '7 months'
print(d,type(d))

# set
# set is immutable data-type
# set is collection of unorder element but each element is uniqeq element not same
s = {11,3,'ketan',6,11,47}
print(s,type(s))