"""
.. module:: numbers
   :platform: Linux, Windows
   :synopsis: Utilities for numbers

.. moduleauthor:: Quentin Marlats

"""

def reduce_id(number):
    """Reduce ID to make it one digit number

    :param number: ID to reduce
    :type number: int
    :returns: reduced number

    """

    return ((number - 1) % 10) + 1
