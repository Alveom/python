from jovian.pythondsa import evaluate_test_cases
tests = []

test = { 
    'input' : {
       'cards': [13 ,11,10,7,4,3,2,1,0],
       'query': 7
    },
    'output' : 3
}
tests.append(test)

tests.append(
    {
        'input': {
            'cards': [13 ,11,10,7,4,3,2,1,0],
            'query': 1
        },
        'output' : 7
    }
)

# if query is infront of  the cards
tests.append(
    {
        'input':{
            'cards': [4 ,2 , 0 , -2],
            'query': 4
        },
        'output' : 0
    }
)
#if query is last of the card

tests.append(
    {
        'input':{
            'cards': [4 ,2 , 0 , -2],
            'query': -2
        },
        'output' : 3
    }
)
#cards does not contains the query

tests.append(
    {
        'input':{
            'cards': [],
            'query': 7
        },
        'output' : -1
    }
)

#query repet

tests.append(
    {
        'input':{
            'cards': [4 ,2 ,1,1,0 -2],
            'query': 1
        },
        'output' : 2
    }
)
tests.append({
    'input':{
        'cards': [4 ,2 ,1,1,0 -2,-9,-5],
        'query': -2
    },
    'output' : 5
})

test

def locate_card(cards, query):
    # for position , cards in enumerate(cards):
    #     if cards == query:
    #          return position
    lo = 0 
    hi = len(cards) -1
    print (hi)
    while lo <= hi :
        mid = (lo + hi )//2

        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            hi = mid - 1
        else : 
            lo = mid + 1
    return -1        
evaluate_test_cases(locate_card , tests)
