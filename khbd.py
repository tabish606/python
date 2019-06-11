guessed_number = int(input("Guess any number :"))
winning_number = 15
if winning_number == guessed_number:
    print('You Win')
else:
    if winning_number < guessed_number:
        print("too high")
    elif winning_number > guessed_number:
        print('too low')