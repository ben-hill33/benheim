# Code Solutions

The implementations I document here are some solutions I found to various code challenges.

## List / Array

??? example "Solutions"

    === "Max Even Number"

        ``` py title="find_max_even.py" 
        # User inputs string w/ numbers: '203 12 5 800 -10'
        user_input = input('Enter numbers:')

        tokens = user_input.split()  # Split into separate strings

        # Convert strings to integers
        nums = []
        for token in nums:
            nums.append(int(token))

        # Print each position and number
        print()  # Print a single newline
        for index in range(len(nums)):
            value = nums[index]
            print('{}: {}'.format(index, value))

        # Determine maximum even number
        max_num = None
        for num in nums:
            if (max_num == None) and (num % 2 == 0):
                # First even number found
                max_num = num
            elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
                # Larger even number found
                max_num = num

        print('Max even #:', max_num)
        ```
    
    === "Reverse a list"

        Reversing a list with bracket notation and pointers.

        - The input is a sequence of characters
        - I create a function that takes in a list, store the first and last index as my start and end pointers, respectively
        - Create a condition that checks while the end of the list is greater than the start of the list, swap indexes
          - Indexes are able to swap by reassigning the value of given index[start], index[end] with index[end], index[start]
        - Note that this solution modifies a sequence, if an argument is passed in that stores a list in random order, the function will return the list as is.

        ``` py title="reverse_list.py"
        def reverse_list(my_list):
            start = 0
            end = len(my_list) - 1

            # swap indexes
            while end > start:

                # while its true that the end is greater than the start
                my_list[start], my_list[end] = my_list[end], my_list[start]

                # Refer to Test Input 1 below
                # start index, being zero, will be plus one, after the switch, will 
                # be 6, 5, 4, 3, 2, 1
                start = start + 1
                # end index, being index five, while loop will break because once the end(right) reaches the middle, the end will no longer be greater than the start
                end = end - 1


        # Test Input 1
        my_list = [1, 2, 3, 4, 5, 6]
        #      <-  ^              ^ ->
        #           \             |
        #    start:[0]       end[5]
        print(reverse_list(my_list))
        # Output 1
        [6, 5, 4, 3, 2, 1]

        # Input 2
        my_list_two = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        print(reverse_list(my_list_two))
        # Output 2
        [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]

        # Input 3
        # my_list_three = range(10)
        # print(reverse_list(my_list_three))
        # Output 3
        TypeError: 'range' object does not support item assignment

        # Input 4.0
        # my_list_four = 'spell this backwards'
        # print(reverse_list(my_list_four))
        # Output 4.0
        TypeError: 'str' object does not support item assignment

        # Input 4.5
        my_list_four = 'spell this backwards'.split()
        print(reverse_list(my_list_four))
        # Output 4.5
        ['backwards', 'this', 'spell']
        ```



