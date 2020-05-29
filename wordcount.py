#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "jodi08 (Jo Anna Mollman)"
# helped by Amanda and Janell

import sys


"""
        make a function for word count

        open and read file

        split file on whitespace

        empty dictionary to store word:count

        loop over file and count words

        add to dictionary



"""


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    new_dict = {}  # empty dictionary to store word:count
    with open(filename) as f:  # open and read file
        for line in f.readlines():
            for word in line.lower().split():
                if word in new_dict:
                    new_dict[word] += 1
                else:
                    new_dict[word] = 1
    return new_dict


"""
call previous function
sort words in dictionary alphabetically
change words to all lowercase
print dictionary word:count
"""


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    word_dict = create_word_dict(filename)
    dict_items = word_dict.items()
    sorted_items = sorted(dict_items)
    for word in sorted_items:
        print(str(word[0]) + ':' + str(word[1]))


def print_top(filename):
    """Prints the top count listing for the given file."""
    new_dict = create_word_dict(filename)
    dict_items = new_dict.items()
    sorted_items = sorted(dict_items, key=lambda x: x[1], reverse=True)
    for word in sorted_items[:20]:
        print(str(word[0]) + ':' + str(word[1]))


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
