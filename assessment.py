# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def total_item_cost(state, cost, tip=0.05):
    """Computating the cost of an item with reference to what state it was purchased in."""

    lowercase_state = state.lower()  # evaluating whether or not the state is 'ca', and making sure string style is the same to avoid error
    if lowercase_state == 'ca':  # if state is California, change tip to 7%
        tip = 0.07

    cost = float(cost)  # use float to avoid calculation/result error
    tip = float(tip)

    tip_calculation = cost * tip  # calculating tip first
    total_calculation = cost + float(tip_calculation)  # summing up total cost and tip to produce final price
    return total_calculation


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

def is_berry(fruit):
    """Checking to see if a fruit is a strawberry, cherry, or blackberry."""

    lowercase_fruit = fruit.lower()  # making sure the fruit string style is checked in the same way as the condition
    if lowercase_fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":  # if any of these berries are called, return true
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
    """We return 0 if berry is a strawberry, cherry, or blackberry; return 5 if something else."""

    fruit = is_berry(fruit)

    if fruit is True:
        return '0'
    else:
        return '5'

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(town):
    """Evaluating whether a town is my hometown or not"""

    town = town.lower()
    if town == "daly city":
        return True
    else:
        return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first, last):
    """Concatenating the first and last name together."""

    return first + ' ' + last

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town, first, last):
    """Greeting a person and checking to see if they are from the same hometown or somewhere else."""

    hometown = is_hometown(town)  # binding is_hometown function to a variable
    name = full_name(first, last)  # binding full_name function to a variable, all for later use

    if hometown is True:  # checking if hometown matches the user
        print "Hi, {}, we're from the same place!".format(name)
    else:
        print "Hi, {}, where are you from?".format(name)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x=1):
    """Incrementing 5 to the original number"""

    def add(y):
        return x + y

    return add  # returning function to make sure it is called within the increment function

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.


addfive = increment(5)  # setting increment to 5
addfive(5)  # running through the function will increase 5 by 5
addfive(20)  # running through the function will increase 20 by 5

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def appending_nums(num, num_list):
    """Appending a single number to a list, where both values are given."""

    num_list = num_list.append(num)  # appending num to the num_list
    return num_list

#####################################################################
