'''
Brief:               Helpers to build the Baby shark anthem

Author:              Simon Rydell
Python Version:      3.7
'''

def wrap_shark(shark):
    """Wrap shark input as a proper baby shark string

    :shark: Input to be wrapped in string
    :returns: Wrapped string
    """
    return f"{shark}, {'doo ' * 6}\n"

def get_sharks():
    """Get the building blocks of the anthem

    :returns: List of strings
    """
    return ["Baby shark", "Mommy shark",
            "Daddy shark", "Grandma shark",
            "Grandpa shark", "Let's go hunt",
            "Run away", "Safe at last", "It's the end"]

if __name__ == '__main__':
    for s in get_sharks():
        print(wrap_shark(s) * 3)
