# ------------------------------------
# makeing a guess game with python ->
# ------------------------------------

""" making a guess game with python and random module
    using while loop and if condition and def function """


# import random module
import random

# define a function for the game
def guess_game():

    """
    make a docstring for -> guess_game function: 
    the function for the game and make a random number
    between 1,9 and count the tries and if want to exit
    the game type exit or 11 and if guess right print the number 
    and tries and if guess wrong print the guess is low or high and if want 
    to exit the game print you exit the game and if want to play again call the function

    """
    
    # welcome massage and instraction for the game
    print(" ------------------------------------")
    print("----- Welcome to the Guess Game -----")
    print(" ------------------------------------")
    print("- the gama for guess a number between 1,9 and count the tries and if want to exit the game type exit or 11 - \n")

    # define a variable for random number
    random_number = random.randint(1, 9)

    # you should make the count 1 not 0 because the first guess not in the loop  
    count = 1
    input_number = int(input("- Enter a number: "))

    # make a while loop for the game
    while input_number != 11 or input_number =="exit" :

        # make first condition for right guess
        if random_number == input_number:
            print("\n- You guess right, the number is {} -".format(random_number))
            print("- Your tries is {} -".format(count))
            loop_agins = input("\n- Do you want to play again? (y/n): ")
            if loop_agins == "y":
                guess_game()
            else:
                break

        # make second condition for input_number in lower than input_number
        elif input_number < random_number:
            print("- Your guess is low -")
            count += 1
            input_number = int(input("- Enter a number: "))
            
        # make second condition for input_number in heigher than input_number
        elif input_number > random_number:
            print("- Your guess is high -")
            count += 1
            input_number = int(input("- Enter a number: "))

        # make a condition for exit the game
    if input_number == 11 or input_number == "exit":
        print("You Exit The Game")
        pass

# call the function
guess_game()