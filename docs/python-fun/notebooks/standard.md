## :material-language-python: Python's Standard Library

Python includes by default a collection of modules that can be imported into new programs. The Python standard library includes various utilities and tools for performing common program behaviors. 

The `math` module provides progress mathematical functions, the `datetime` module provides date and calendar capabilities, the `random` module can produce random numbers, the `sqlite3` module can be used to connect to SQL databases, and so on. Before starting any new project, good practice is to _research what is available in the standard library_, or on the internet, to help complete the task. Methods to find many more useful modules made available on the internet by other programmers are discussed in another section.

??? example "Commonly used Standard Library Modules"

    | Module name 	|                               Description                               	|                Documentation link               	|
    |:-----------:	|:-----------------------------------------------------------------------:	|:-----------------------------------------------:	|
    | datetime    	| Creation and editing of dates and times objects                         	| [datetime docs](https://docs.python.org/3/library/datetime.html )	|
    | random      	| Functions for working with random numbers                               	| [random docs](https://docs.python.org/3/library/random.html)   	|
    | copy        	| Create complete copies of objects                                       	| [copy docs](https://docs.python.org/3/library/copy.html  )   	|
    | time        	| Get the current time, convert time zones, sleep for a number of seconds 	| [time docs](https://docs.python.org/3/library/time.html  )   	|
    | math        	| Mathematical functions                                                  	| [math docs](https://docs.python.org/3/library/math.html  )   	|
    | os          	| Operating system informational and management helpers                   	| [os docs](https://docs.python.org/3/library/os.html    )   	|
    | sys         	| System specific environment or configuration helpers                    	| [sys docs](https://docs.python.org/3/library/sys.html   )   	|
    | pdb         	| The Python interactive debugger                                         	| [pdb docs](https://docs.python.org/3/library/pdb.html   )   	|
    | urllib      	| URL handling functions, such as requesting web pages                    	| [urllib docs](https://docs.python.org/3/library/urllib.html)   	|

??? note "Some Code Examples"

    === "datetime"

        The datetime module prints the day, month, and year of a date that is a user-entered number of days in the future.

        ```py
        import datetime

        # Create a new date object representing the current date (May 30, 2016)
        today  = datetime.date.today()

        days_from_now = int(input('Enter number of days from now: '))

        # Create a new timedelta object that represents a difference in the 
        # number of days between dates.
        day_difference = datetime.timedelta(days = days_from_now)

        # Calculate new date
        future_date = today + day_difference

        print(days_from_now, 'days from now is', future_date.strftime('%B %d, %Y'))
        ```

    === "random"

        The random module is used to implement a simple game where a user continues to draw from a deck of cards until an ace card is found.

        ```py
        import random

        # Create a shuffled card deck with 4 suites of cards 2-10, and face cards
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)

        num_drawn = 0
        game_over = False
        user_input = input("Press any key to draw a card ('q' to quit): ")
        while user_input != 'q' and not game_over:

            # Draw a random card, and remove card from the deck
            card = random.choice(deck)
            deck.remove(card)
            num_drawn += 1

            print('\nCard drawn:', card)

            # Game is over if an ace was drawn
            if card == 'A':
                game_over = True
            else:
                user_input = input("Press any key to draw a card ('q' to quit): ")

        if user_input == 'q':
            print("\nGame was quit")
        else:
            print(num_drawn, 'card(s) drawn to find an ace.')
        ```

??? example "`import module` vs `from module import names`"

    |             Description            	|     Example import statement    	|    Using imported names    	|
    |:----------------------------------:	|:-------------------------------:	|:--------------------------:	|
    | Import an entire module            	| `import HTTPServer `              	| `print(HTTPServer.address)`  	|
    | Import specific name from a module 	| `from HTTPServer import address`  	| `print(address) `            	|

All names from a module can be imported directly by using a `*` character, as in the statement `from HTTPServer import *`.

A common error is to use the `import *` syntax in modules and scripts, which makes identification of dependencies and the origins of variables difficult for a reader of the code to understand. Good practice is to limit the use of `import *` syntax to interactive interpreter sessions.
