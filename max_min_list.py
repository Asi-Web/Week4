## Asiwome Agbleze
## CMSC 111
## Spring 2026
## Week 4 Assignment

## This function finds the largest and smallest number in a list
def find_max_min(num_list):
    # Check if the list is empty before using max() and min()
    if len(num_list) == 0:
        print("Error: The list is empty.")
    else:
        largest = max(num_list)
        smallest = min(num_list)


        print("Largest number:", largest)
        print("Smallest number:", smallest)


    try:
        # Use the list exactly as shown in the assignment
          numbers = [4, 7, 1, 9, 3]

        # Call the function
        find_max_min(numbers)

except Exception as e:
    print("An error occurred:", e)