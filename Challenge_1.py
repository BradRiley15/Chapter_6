def ask_number(question, low, high, step = 1):
    guess = None
    while guess not in range(low, high):
        guess = int(input(question))
    return guess

