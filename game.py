from random import randint
def main():
    print("Welcome to coin flip game!")
    check = "yes"
    while(check != "no"):
        random_number =  randint(1, 2) 
        guess = input("Guess the coin flip result (1 for heads, 2 for tails): ")
        if guess == str(random_number):
            print("Congratulations! You guessed it right!")
        else:
            print("Sorry, you guessed it wrong.")
        check = input("Do you want to play again? (yes/no): ")       

main()