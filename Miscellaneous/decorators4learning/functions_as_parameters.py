def g():
    print("Hi, it's me the awesome function called 'g'")
    print("Thanks for calling me!")


def f(func):
    print("Hi, I am the amazing function called 'f'.")
    print("I will call 'func' now.")
    func()
    print("func's real name is " + func.__name__)


f(g)
