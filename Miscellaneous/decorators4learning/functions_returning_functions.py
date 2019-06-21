def f(x):
    """ This function returns the function 'g' which is inside function. """
    def g(y):
        return y + x + 3 
    return g


nf1 = f(1)
nf2 = f(3)

print(nf1(1))
print(nf2(1))
