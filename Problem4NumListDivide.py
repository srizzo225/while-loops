#Sara Margaret Rizzo
#2020-09-06

#Problem 4: Create a while loop that initializes a counter at 0 
#and will run until the counter reaches 50. If the value of the counter is divisible by 10, 
#append the value to the list called tens. Confirm the list results using a print statement.

#create list
tens = []

#create function
def numlist():
    #start counter at 0
    counter = 0
    #stop when the counter reaches 50
    while counter < 50:
        #add 1 to the counter
        counter = counter + 1
        #if the new number is divisible by 10, add it to the list
        if counter %10 == 0:
            tens.append(counter)

#call function and print list
numlist()
print(tens)