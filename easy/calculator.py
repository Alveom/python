def userInput():
    opreList= ['+','-','*','/']


    while True : 
        num1Ex = input('please enter the first number : ')
        if num1Ex.isdigit():
            num1 = int(num1Ex)
            

        else :
            print('Invalid input , please enter a number')
            continue
            
        num2Ex = input('please enter the second number : ') 
        if num2Ex.isdigit():
            num2 = int(num2Ex)

        else :
            print('Invalid input , please enter a number')
            continue
        
        opre = input('please enter the operator : ')
        if opre not in opreList:
            print('Invalid operator , please enter one of the following : + , - , * , /')
            continue

        else :

            return num1 , num2 , opre
            

        


def calculation():
    num1 , num2 , oper = userInput()
    if oper == '+':
        sum = num1 + num2 
    elif oper == '-':
       sum =  num1 - num2 

    elif oper == '*':
       sum =  num1 * num2
    
    elif oper == '/':
        sum = num1 / num2 
    else :
         print ('This fuction is not added')
    
    print (f'the oparation of {num1} {oper} {num2} = {sum}')
    return sum 



def main():
    calculation()


main()