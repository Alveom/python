from jovian.pythondsa import evaluate_test_cases

tests = []

# Defining a test case
tests.append({
    'input': {
        'numbers': 123456789
    },
    'output': 987654321
})

tests.append({
    'input': {
        'numbers': 987456123
    },
    'output': 321654789
})

tests.append({
    'input': {
        'numbers': 1200
    },
    'output': 21
})

tests.append({
    'input': {
        'numbers': 500
    },
    'output': 5
})

tests.append({
    'input': {
        'numbers': 1001
    },
    'output': 1001
})

tests.append({
    'input': {
        'numbers': 4500
    },
    'output': 54
})

tests.append({
    'input': {
        'numbers': 12321
    },
    'output': 12321
})

tests.append({
    'input': {
        'numbers': 0
    },
    'output': 0
})

tests.append({
    'input': {
        'numbers': 1
    },
    'output': 1
})


# Fix the function to take only one argument: numbers
def number_reverse(numbers):
    return int(str(numbers)[::-1])

# Main function to run the test cases
def main():
    evaluate_test_cases(number_reverse, tests)

# Running the main function
if __name__ == "__main__":
    main()

