def count_even(lst):
  
    count = 0 

    for i in range(len(lst)):
        num = lst[i]
        if num % 2 == 0:
            count += 1
    print(f"Number of even numbers: {count}")   # Print out how many even numbers we counted above

def get_list_of_ints():

    lst = []  # Make an empty list to store integers

    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer

    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  # Convert user input into an integer and add to list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)


if __name__ == '__main__':
    main()