#Sara Margaret Rizzo
#2020-09-06

#Problem 3: Using a while loop, ask the user to enter a number. 
#Append each entered number to a list and add them together. 
#Continue asking for a number until the sum of the list of numbers is greater than 100.

#empty list
L= []

#function to fill list
def sumlist(L):    
    #start counter at 0
    sum = 0
    #continue adding to the list until the sum is greater than 100
    while sum <= 100:
        #ask user for a new number to add to list
        x = int(input("Enter a number:"))
        #add input to list
        L.append(x)
        #add new input to running total
        sum = sum + x
    #return back the new list
    return sum

#print the total, then the list
print(sumlist(L))
print(L)