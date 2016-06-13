#    __                      _       __       _
#   / / _   _  ___ ___ _ __ | |_    / /  __ _| |__
#  / / | | | |/ __/ _ \ '_ \| __|  / /  / _` | '_ \ 
# / /___ |_| | (__  __/ | | | |_  / /___ (_| | |_) |
# \____/\__,_|\___\___|_| |_|\__| \____/\__,_|_.__/
#
# Author: Jesse Goble
# 2016
#
# Usage pseudocode:
# >>> course_obj
# >>> course_list = Courses()
# >>> course_list.addCourse(course_obj)
# >>> course_obj_list = course_list.returnCourses()
#
 
__author__ = "Jesse Goble"
__version__ = "1.0"

class Courses(object):
  """
  This is a simple container Class for Course Class objects
  """

  def __init__(self, course=None):
    """
    This initializes the class and sets the class variable of course_list
    to NULL.
      
    Arguments:
      -course (optional[Course Class object]): An optional Course Class can be
      passed during Courses creation.
    """

    self.course_list = []

    if (course is not None):
      self.course_list.append(course)

  """
  Setter
  """

  def addCourse(self, course):
    self.course_list.append(course)

  def clearAllCourses(self):
    self.course_list = []

  """
  Getter
  """

  def returnCourses(self):
    return self.course_list

  """
  Print List
  """

  def printCourses(self):
    for c in self.course_list:
      c.printCourse()
