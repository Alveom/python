import random

print('Welcome to the game of Rock, Paper, Scissor. Rules are the same and we have a working score system')


computerList = ['rock' , 'paper', 'scissor']
computerRandom = -1

maxNumber , lowNumber = 0 , 2
score = 0 
comScore = 0 
ywon = 0 
cwon = 0 
draw = 0

while True:
    userInput = input('Enter your choice [rock , paper , scissor or q of quite]: ')
    


    compRan = random.randint(maxNumber , lowNumber)
    computerRandom = computerList[compRan]


    if userInput == 'q':
        print('Thank you for playing. Goodbye!')
        print('Your score: ', score)
        print('Computer score: ', comScore)
        print(f'you won {ywon} computer won {cwon} the amount of draw {draw}')
        quit()

   
    if userInput not in computerList:
        print('invalid input plz try again: ')
        continue
     
    print(f"You choce '{userInput}' and Computer choce '{computerRandom}'" )
        

    if userInput == computerRandom:
        print('It is a tie!')
        score += 0.5
        comScore += 0.5
        draw += 1


    elif userInput == 'rock' and computerRandom =='scissor':
        print('You win!')
        score += 1
        ywon += 1
    elif userInput == 'paper' and computerRandom == 'rock':
        print('You win!')
        score += 1
        ywon += 1
    elif userInput == 'scissor'  and computerRandom == 'paper':
        print('You win!')
        score += 1
        ywon += 1
    else :
        print('computer won!')
        comScore += 1 
        cwon += 1

   


