import random;
import os;


def game_result(computer, user):
    #water and snake
    if(computer == 'w' and user == 's'):
        return True
    if(computer == 's' and user == 'w'):
        return False
    #snake and gun
    if(computer == 'g' and user == 's'):
        return False
    if(computer == 's' and user == 'g'):
        return True    

    #gun and water
    if(computer == 'w' and user == 'g'):
        return False
    if(computer == 'g' and user == 'w'):
        return True


user = input("Choose your equipment Water(w) Snake(s) Gun(g):").lower()

rand_num = random.randint(1,3)
    
if(rand_num == 1):
    computer = 's';  
 
elif (rand_num == 2):
    computer = 'w';

else:
    computer = 'g';
  

result = game_result(computer, user)
print(f"You chose {user}", )
print(f"Computer chose {computer}", )

if(result is None):
    print("It's a draw");
elif(result == True):
    print("You won")
else:
    print("Computer won")