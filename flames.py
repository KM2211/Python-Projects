
def flame(name1, name2):
    word = 'FLAMES'
    
    status = {
        'F' : 'Friends',
        'L' : 'Love',
        'A' : 'Affection',
        'M' : 'Marriage',
        'E' : 'Enemy',
        'S' : 'Siblings'
    }
    
    total_unique_letters = set(''.join(sorted(set(name1.lower()))) + ''.join(sorted(set(name2.lower()))))

    flame_key = (len(total_unique_letters) % 6) -1
    
    print("Relationship Status: ", status.get(word[flame_key]))

name1 = input("Enter first name : ")
name2 = input("Enter second name : ")


flame(name1, name2)


