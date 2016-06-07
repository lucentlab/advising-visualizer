#    __                      _       __       _
#   / / _   _  ___ ___ _ __ | |_    / /  __ _| |__
#  / / | | | |/ __/ _ \ '_ \| __|  / /  / _` | '_ \
# / /___ |_| | (__  __/ | | | |_  / /___ (_| | |_) |
# \____/\__,_|\___\___|_| |_|\__| \____/\__,_|_.__/
#
# A collection of functions used by the FAP project.
#
# Author: Jesse Goble
# 2016
#
# Usage pseudocode:
#
#

__author__  = "Jesse Goble"
__version__ = "1.0"

def is_number(num):
  """
  This function checks to see if a specified variable holds a float.
  Arguments:

    num (any): The value to check.
  """

  try:
    float(num)
    return True
  except ValueError:
    return False
