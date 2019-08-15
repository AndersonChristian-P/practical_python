def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


# #### 


print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) >= 4:
        print('That is alot of cats.')
    else:
        print ('That is not that many cats')
except ValueError:
    print('You did not enter a number')
    

# errors cause the program to crash
# an error that happens inside a try block will cause code in the except block to execute. that code can handle the error or display a message to the user so that the program can keep going
