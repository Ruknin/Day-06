# syntex of for loop
""" 
for val in sequence:
    body of for
"""
#printing 0 to 4
'''for x in range(5):
    print(x)'''

#printing from 4 to 12
'''for x in range(4,13):
    print(x)'''

#printing 2 to 100 only even numbers
for x in range(1,101):
    if x %2 ==0:
        print(x, end = ' \t' )
