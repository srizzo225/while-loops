#Sara Margaret Rizzo
#2020-09-06

#Problem 2: Using a while loop, create a list called L that contains the numbers 0 to 10. 
#On each iteration, the loop should append the current value of a counter variable to the list 
#and then increase the counter by 1. 
#The while loop should stop once the counter variable is greater than 10.

#empty list
L= []

#function to fill list
def addlist(L):
    #start with zero
    x = 0
    #the list should only go up to 10
    while x <= 10:
        #add the current value to the list
        L.append(x)
        #add one to x for the next pass through the loop
        x = x + 1
    #return back the new list
    return L

#print the list
print(addlist(L))
