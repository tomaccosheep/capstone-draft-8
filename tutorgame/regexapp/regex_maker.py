import random
import string
import re

class Regexer:
    # This is a list of types and matching regex. This dictionary is used
    # to create the regex string and the findme string
    # {{
    regex_dict = {'digit': '\d', 'single_char': '[a-zA-Z]', 'space': '\s'}
    # }}

    # This is a list of all opened types of regex
    # {{
    open_regex = ['digit', 'single_char', 'space']
    # }}

    # This creates the Regexer object with args representing
    # regex types that could be in the open_regex list
    # {{
    def __init__(self, *args):
        for arg in args:
            if arg not in open_regex:
                open_regex.append(arg)
    # }}

    # This takes in a regex type and outputs characters that
    # correspond for that type. Used for building answer strings.
    # {{
    def regex_step_function(self, func_key):
        if func_key == 'single_char':
            return random.choice(string.ascii_letters)
        elif func_key == 'digit':
            return str(random.randrange(0,10,1))
        elif func_key == 'space':
            return ' '
    # }}

    # This takes in a regex_list and shortens it, so
    # that two instances will return one instance
    # with a coefficient
    # {{ 
