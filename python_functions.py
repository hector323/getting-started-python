def is_even(number):
    return number % 2 == 0


def select_even(elements):
    '''
    Iterate through the numbers one by one, and for each number, check if that number is even. If it's even then append the element to a new list of even numbers.
    '''
    selected = []
    for element in elements:
        if is_even(element):
            selected.append(element)
    return selected


# Find what's common
def ends_ing(word):
    '''
    Returning a subset of elements that meet a specific criteria is something commonly done in Python. And the procedure looks pretty much the same regardless of what we are selecting. For example, let's now select words that end with 'ing'.
    '''
    return word.endswith('ing')

def select_ing(elements):
    selected = []
    for element in elements:
        if ends_ing(element):
            selected.append(element)
    return selected

words = ['camping', 'biking', 'sailed', 'swam']
select_ing(words)

def find_initial(name):
    '''
    As you may have guessed, using a for loop to alter each element by applying some operation is a common procedure in programming. Let's write a function that derives the initials of each person's name.
    '''
    names = name.split(' ')
    first_name = names[0]
    last_name = names[1]
    return first_name[0] + last_name[0]

def find_initials(elements):
    altered = []
    for element in elements:
        altered.append(find_initial(element))
    return altered

# find_initials()

def greet_employees():
    welcome_messages = []
    for new_employee in new_employees:
        welcome_messages.append("Hi " + new_employee.title() + ", I'm so glad to be working with you!" )

    return welcome_messages