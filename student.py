#    __                      _       __       _
#   / / _   _  ___ ___ _ __ | |_    / /  __ _| |__
#  / / | | | |/ __/ _ \ '_ \| __|  / /  / _` | '_ \ 
# / /___ |_| | (__  __/ | | | |_  / /___ (_| | |_) |
# \____/\__,_|\___\___|_| |_|\__| \____/\__,_|_.__/
#
# Student class object models an individual Wilkes University student's
# academic progress towards degree completion. Functions are included to
# build the student's required classes for their degree as well as 
# parse the text from their unofficial transcript for such information.
#
# Dependancies:
#   - Course:   Class Object for modeling a Wilkes University course.
#   - Courses:  Class Object for storing a variable number of Course objects.
#   - FAPlib:   Library file. Currently needed for the function is_number.
#   - re:       Regular Expressions library
#   - csv:      Reading CSV files.
#
# Author: Jesse Goble
# 2016
#
# Usage pseudocode
#
# Imports
from __future__ import print_function
from course import Course
from courses import Courses
import FAPlib
import re
import csv

__author__    = "Jesse Goble"
__version__   = "1.0"
 
class Student(object):
  """
  This is a class object holding information about a Wilkes University
  Student. A Wilkes Student has:
    - major: A two or three letter designation for the program they're
      enrolled in.
    - major_reqs: A list of Course objects (Courses) built from a CSV file
      related to the program they're enrolled in.
    - taken_courses: A list of Course objects (Courses) parsed from a
      cut-and-copy version of their unofficial transcript. 
  """

  def __init__(self, major=None):
    """
    Creates an empty version of the Student object.
    """

    self.major          = major
    self.major_reqs     = Courses()
    self.taken_courses  = Courses()

  def defineMajorReqs(self, file=None):
    """
    Opens a specified CVS file and builds a Courses list object of those
    classes.

    Arguments:
      - file (Optional[str]): The filename of the CSV file for the major.
          If not specified and the student's major is set, then file will be
          set automatically.
    """

    if (self.major is not None and file is None):
      if (self.major == "PHY"):
        file = "DATA/required_PHY_courses.csv"
      elif (self.major == "CS"):
        file = "DATA/required_CS_courses.csv"
      elif (self.major == "EE"):
        file = "DATA/required_EE_courses.csv"
      elif (self.major == "IM"):
        file = "DATA/required_IM_courses.csv"
      #elif (self.major == ""):
      #  file =
    elif (file is None):
      raise ValueError("Either set the student's major or specify a Major Requirements file to use.")
        

    with open(file) as csvfile:
      reader = csv.reader(csvfile)
      for line in reader:
        if (not re.search("^#", line[0])):
          course_obj = Course(line[0], line[1], line[2], line[3], False, None,
                        line[4], line[5])
          self.major_reqs.addCourse(course_obj)

  def processMajorReqs(self, file):
    """
    Using the defined major requirments, parses the users transcript and 
    determines if this student has taken or is taking a required major course
    and sets information for that Course object.
    """

    with open(file) as student_file:
      for line in student_file:
        for course in self.major_reqs.returnCourses():
          #print("\t\t" + course.returnCourseId() + ":")

          (this_course, course_num) = course.returnCourseId().split("-")

          if (re.search(this_course + r'\s{1,3}' + course_num, line)):
            course.setTaken(True)
            returned_line = line.split()
            if (returned_line[-1] == "TR" or returned_line[-1] == "W"
             or (FAPlib.is_number(returned_line[-1])
                and float(returned_line[-1]) >= 0.0
                and float(returned_line[-1]) <= 4.0)):
              course.setGradeEarned(returned_line[-1])
  
  def parseTranscript(self, file):
    """
    Parses the student's unofficial transcript and builds a Courses object
    of all the classes in the transcript.
    """

    with open(file) as student_file:
      # Initialize Sentinel - For most classes, Credit Hours and Quality Points
      #   show up over two lines.
      sentinel = 0

      for line in student_file:
        # Skip empty lines.
        if (re.match(r'^\s+$', line)):
          continue

        # We've reached the two trailing lines, so reset the sentinel.
        if (sentinel > 1):
          sentinel = 0

        if (re.search(r'[A-Z]{2,3}\s{1,3}(?:\d{3}|ELE)\s', line)
            or sentinel > 0):
          if (sentinel == 0):
            sl = line.strip().split()
            #print(sl[2:-1])
            if (sl[2] == "UG"):
              course_name = " ".join(map(str, sl[3:-1]))
            else:
              course_name = " ".join(map(str, sl[2:-1]))

            course_obj = Course(sl[0] + "-" + sl[1], course_name, 0, 0,
                                  True, sl[-1])
          elif (sentinel == 1):
            val = line.strip().split()
            course_obj.setCredits(val[-1])
            self.taken_courses.addCourse(course_obj)
          sentinel += 1

  """
  Setters
  """

  def setMajor(self, which_major):
    self.major = which_major

  """
  Getters
  """

  def returnMajor(self):
    return self.major

  def returnMajorReqs(self):
    return self.major_reqs.returnCourses()

  def returnCourses(self):
    return self.taken_courses.returnCourses()

  """
  Print functions
  """

  def printMajorReqs(self):
    for course_obj in self.major_reqs.returnCourses():
      print("Course ID: " + course_obj.returnCourseId(), end=" ")
      print("Course Name: " + course_obj.returnCourseName())
      print("Credits: " + course_obj.returnCredits(), end=" ")
      print("Semester: " + course_obj.returnSugSemester(), end=" ")
      # Need to loop through Courses List here.
      #print("Pre Requesites " + course_obj.returnCoursePrereqs())
      #print("Co Requesites " + course_obj.returnCourseCoreqs())
      print()

  def printCourses(self):
    self.taken_courses.printCourses()
    #for c in self.taken_courses.returnCourses():
    #  c.printCourse()
