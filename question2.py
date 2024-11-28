# QUESTION 2
def sorted_ascending(list):

    if list == sorted(list):
        print(True)

    else:
        print(False)    

sorted_ascending([11,12,13,14,15]) #Sorted list will return True
sorted_ascending([13,12,17,14,15]) #Un-Sorted list will return False