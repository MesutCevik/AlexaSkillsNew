def temperatur(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It is " + str(celsius2fahrenheit(t)) + " degrees."

    return result


print(temperatur(20))
