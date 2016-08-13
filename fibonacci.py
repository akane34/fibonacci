topNumber = int(raw_input("Enter the top number here: "))

def fibonacci(endNumber):
    left = 0
    right = 1
    result = 0
    while 1 == 1:
        result = left + right
        left = right
        right = result

        if result < endNumber:
            print result
        else:
            break

fibonacci(topNumber)