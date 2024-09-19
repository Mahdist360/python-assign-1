import random
import sys

def random_generator():
    
    try:
        random_number = random.randint(0, 100)
    
    except Exception as e:
        print('An Error Occured')
        return sys.exit()
    
    else:
        return random_number


def prompt():


    try:
        user_input = input('Enter your guess: ')
        user_input = int(user_input)

    except Exception as e:
        print('An Error Occured')
        return sys.exit()
    
    else:
        return user_input




def game():
    attempts = 0
    random_number = random_generator()
    user_guess = prompt()
    while(True):
        
        try:
            if(user_guess != random_number ):
                attempts += 1
            if((user_guess - random_number) > 30): print('Too High')
            if((random_number - user_guess ) > 30): print('Too Low')
            if(abs(random_number - user_guess) <= 30): print('Near to the ans')
            user_guess = prompt()
            if(user_guess == random_number ):
                print("Congratulations! You've guessed the number in" + attempts + "attempts.")
                return
        except Exception as e:
            print('An Error Occured')
            return sys.exit()
            

game()
        

