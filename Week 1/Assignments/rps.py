import random
print("You are playing game with the computer")
player_name=input("Enter your name: ")
options = ['rock','scissor','paper']
i=0
player1_score=0
player2_score=0
while i<5:
    player1= input("Choose any one between rock, scissor and paper: ")
    player2= random.choice(options)
    
    if player1 == player2:
        print('player2: ',player2)
        print('TIE')
        
    elif player1 =='scissor':
        if player2 =='rock':
            print('player2: ',player2)
            print('you loose')
            player2_score+=1
        else:
            print('player2: ',player2)
            print('you won')  
            player1_score+=1
        
    elif player1=='rock':
        if player2=='paper':
            print('player2: ',player2)
            print('you loose')      
            player2_score +=1
        else:
            print('player2: ',player2)
            print('you won')
            player1_score+=1 
    
    elif player1=='paper':
        if player2=='scissor':
            print('player2: ',player2)
            print('you loose')
            player2_score+=1
        else:
            print('player2: ',player2)
            print('you won')
            player1_score+=1

    else:
        print('Error')
        continue
    i = i+1
         
if player1_score>player2_score:
    print('You won',player_name,'with score',player1_score)
elif player1_score<player2_score:
    print("You loose",player_name,'with score',player1_score) 
else :
    print('Tie with score',player1_score)  