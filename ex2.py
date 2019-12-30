'''
purpose: function example2
'''
def is_prime():
     pass
def is_even(num=57):
     '''
    check num is even or odd
     '''
     if num%2 == 0:
        return "EVEN NUMBER %s"%(num)
     else:
        return"ODD NUMBER %s"%(num)
print(is_even())