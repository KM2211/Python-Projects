import random

MOVIES = ["Baazigar", "Darr", "Lagaan", "Devdas", "Maqbool", "Paheli", "Fiza", "Taal", "Jism", "Saathiya", "Pardes", "Kaal", "Company", "Nagina", "Lamhe"]



def strike(n):
    text = "BOLLYWOOD"
    result = ''
    for i in range(n):
        result = result +text[i] + '\u0336'
    return(result)
    
def bollywood():
    bollywood = "BOLLYWOOD"
    print(f'\n {bollywood}')
    
    full_word = {}
    tries = 9
    count =0
    duplicates = set()

    movie_name = random.choice(MOVIES)
    no_of_letters = len(movie_name)
    words = [''] * no_of_letters
    
    for i in range(no_of_letters):
        print("_",end=" ")
        
    print("\n")
    
    while (tries):
        letter = input("\nEnter a letter - ")
        
        letter = letter.upper()
        indices = [i for i, char in enumerate(movie_name.upper()) if char == letter]
        
        full_word[letter] = indices
        
        if letter in duplicates:
            print("You have already guessed it! Try a new letter \n")
        else:
            duplicates.add(letter)
            for key, value in list(full_word.items()):
                if value:
                    for i in value:
                        words[i] = key
                else:
                    tries = tries - 1
                    count = count+1
                    bollywood = strike(count)
                    
                    del full_word[key]
                    print(bollywood)
                    
        final_word = ''.join(words)
        
        if final_word.lower() == movie_name:
            tries = 0
            print("\n YAYYY YOU WON!!!")
            
            
        if count  == 9:
            tries = 0
            print("TRY AGAIN NEXT TIME!!!")
            print("The Movie name was  - ", movie_name)
        else:
            for i in words:
                if i:
                    print(i, end=" ")
                else:
                    print("_", end= " ")
        
        print("\n")
    
print("Welcome to Bollywood!!!")
print("\n Rules \n")
print("-> You have 9 tries as of Bollywood.")
print("-> Each wrong letter reduces your number of tries.")
print("-> Each correct letter takes you one step closer to victory")
print("-> Guess the Movie and win the game. All the Best \n")
print("~~~~~~~~~~Lets start!!!~~~~~~~~~~~~~~~~~~~~~~\n")
name = input("Enter you name - ")
print(f'Hey {name}, Lets play Bollywood!!!')




bollywood()


