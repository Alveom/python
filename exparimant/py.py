import random 

def randomNumber():


   
    while True :
        un = random.randint(4,50)
        print(un)
        if un == 50:
            print('Its the highest it can get')
        elif un == 4:
            print('the lowest it can get')
        elif un == 25:
            print('we fonud what we were looking for')
            break 
        elif un == 30 :
            print('You are close to find the number that will break the loop')

       



randomNumber()