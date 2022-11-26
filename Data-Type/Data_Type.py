x = 10
y = 7.333
z = 1+2j

# int
print(x,' is Data-Type equal to ',type(x))

# float
print(y,' is Data-Type equal to ',type(y))

# complex number
print(z,' is Data-Type equal to', type(z))

# string
s = 'ketan'
print(s,type(s))
s = '''
        Good, Morning
        Hello, My name is ketan
        what are doing?
    '''
print(s,type(s))

# List Data-Type
l = [1,'ketan',4.768786,[2,46,75],(55,433,1+3j)]
print(l,type(l))
l[3][0] = [11,22,33,44]
print(l,type(l))

# Tuple
t = (11,2,'hello',2+3j,'hgjjj')
print(t,type(t))
# t[0] = 'ketan' here tuple data-type is not mutable data-type so it can't be update the tuple value
#  and tuple data-type is  faster than list data-type

