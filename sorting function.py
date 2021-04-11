'''
Program finds the smallest value in a list, and moves it to another list via
n elements, WITHOUT the use of the sort or sort function.
'''
#Input - Function reads numbers given until -1 is entered, and appends them
def get_int(alist):
    while True:
        try:
            n = int(input("Enter an integer for the list & type -1 when done: "))
            #Exits when -1 is entered.
            if n == -1:
                return alist
            else:
                alist.append(n)
        except:
            print("Please enter an actual number!")

#Process - Sorts the list without using the sort/sorted function
def selectionSort(alist):
    ordered = []

    #Searches elements in alist until it's empty.
    while not(alist == []):
        #Assigns the smallest value in alist a variable.
        smallest = min(alist)
        #Assigns the smallest value's index in alist a variable.
        smallestPos = alist.index(min(alist))
        #Appends the smallest value in alist to the ordered list.
        ordered.append(smallest)
        #Deletes the position of the smallest value's index in alist, so it
        #doesn't pick the same value again.
        del(alist[smallestPos])
        
    return ordered



'''MAIN PROGRAM'''
alist = []

#Output - Sorts the list
print("This program will sort the given numbers in a list")

#Retrieves input for n elements and adds them to a list.
theList = get_int(alist)

#Sorts the list of n elements.
ordered = selectionSort(theList)
print(f"The ordered list is {ordered}")


