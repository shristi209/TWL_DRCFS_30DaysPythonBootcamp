print("lets start our game")
user1=input('choose betn three rock, scissor, paper')
game=user1 
user2=input('choose betn three rock, scissor, paper')
game2=user2
if game=='rock' and game2=='rock':
    print("Tie")
elif game=='rock' and game2=='paper':
    print('paper win')
elif game=='paper' and game2=='rock':
    print('paper win')
elif game=='rock' and game2=='scissor':
    print('rock win')
elif game=='scissor' and game2=='rock':
    print('rock win')
elif game=='paper' and game2=='paper':
    print('tie')
elif game=='scissor' and game2=='scissor':
    print('scissor')
elif game=='scissor' and game2=='paper':
    print('scissor win')
elif game=='paper' and game2=='scissor':
    print('scissor win')
else:
    print('error')
