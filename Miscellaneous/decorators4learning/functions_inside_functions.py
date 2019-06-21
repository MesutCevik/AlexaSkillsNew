def f():
    """ Diese Funktion beinhaltet 1.) eine andere Funktion u. 2.) printed es zwei Zeilen Text aus u. 3. ruft es
    die enthaltene Funktion einmal auf. """

    def g():
        # Diese Funktion printed nur zwei Zeilen Text aus.
        print("Hi, it's me the awesome function called 'g'")
        print("Thanks for calling me!")

    print("This is the amazing function called 'f', which contains the function 'g' inside.")
    print("I am calling the other function now, it's 'g'.")
    g()


f()
