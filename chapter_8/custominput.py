import pyinputplus as p

def uptoten(numbers):
    numbersLIST = list(numbers)
    for i, digit in enumerate(numbersLIST):
        numbersLIST[i] = int(digit)
    if sum(numbersLIST) != 10:
        raise Exception('the digits don\'t add up to 10, it adds upto %s', sum(numbersLIST))
    return(int(numbers))

response = p.inputCustom(uptoten)
print(response)
