#    __                      _       __       _
#   / / _   _  ___ ___ _ __ | |_    / /  __ _| |__
#  / / | | | |/ __/ _ \ '_ \| __|  / /  / _` | '_ \ 
# / /___ |_| | (__  __/ | | | |_  / /___ (_| | |_) |
# \____/\__,_|\___\___|_| |_|\__| \____/\__,_|_.__/
#
# The Course class object models a specific, unique Wilkes University course.
#
# Author: Jesse Goble
# 2016
#
# Usage pseudocode:
#
#
# Imports
from __future__ import print_function
import re

__author__ = "Jesse Goble"
__version__ = "1.0"

class Course(object):
  """
  This is a class object holding all information pertaining to a Wilkes
  University Course. The Course object was designed to work as a child 
  class of the Student class with multiple class objects being held in a
  Courses class object.

  As the Course class object holds information pertaining to a particular
  Student's course, grade and taken attributes are stored here. If used in 
  a more generic fashion, just ignore those attributes.
  """
  def __init__(self, course_id, course_name, credits=0, sugg_semester=0, taken=False, earned_grade=-1.0, course_prereq=None, course_coreq=None, requires_senior_standing=False, requires_dept_approval=False):
    """
    This will create an instance of the class and set required attributes.

    Arguments:
      -course_id (str): This is a valid Wilkes University course id in the
        format MTH-102 or EE-283.

      -course_name (str): This is the title of the course, such as
        Calculus II or Electrical Measurements Lab.

      -credits (Optional[int]): The number of credits for the course. Default
        to 0 unless specified.

      -sugg_semester (Optional[int]): An integer enumeration for the suggested
        semester that the class should be taken. 1 indicates the 1st year,
        first semester while 8 indicates 4th year, second semester. Only used
        for courses required by major. A value of 0 will indicated electives
        or other courses.

      -taken (Optional[bool]): A boolean value indicating that the course
        was taken.

      -earned_grade (Optional[float]): The grade earned for the class on 
        the 4.0 scale. Special cases: W indicates that the course was 
        withdrawn from, TR indicates that the course was tranferred from
        another school, None indicates that the course is in progress.
        Quality points will not be calculated for any course falling in one of
        these special cases.

      -course_prereq (Optional[list[str]): Listing of courses that need
        to be completed prior to enrollment to this course. Using a list as
        the only information known is the course id.

      -course_coreq (Optional[list[str]): Listing of courses that must
        be taken at the same time as this course. Using a list as the only 
        information known is the course id.

      -requires_senior_standing (Optional[bool]Optional[): Flag that the class
        requires 'senior standing' to take.

      -requires_dept_approval (Optional[bool]): Flag that the class requires
        approval from the department head or other person prior to enrollment.

    """

    self.course_id = course_id
    self.course_name = course_name
    self.credits = credits
    self.sugg_semester = sugg_semester
    self.taken = taken
    self.earned_grade = earned_grade

    self.course_prereq = []
    # The CSV may have multiple entries, separated by ':'
    if (course_prereq and re.search(":", course_prereq)):
      for word in course_prereq.split(":"):
        self.course_prereq.append(word)
    else:
      self.course_prereq.append(course_prereq)

    self.course_coreq = []
    # The CSV may have multiple entries, separated by ':'
    if (course_coreq and re.search(":", course_coreq)):
      for word in course_coreq.split(":"):
        self.course_coreq.append(word)
    else:
      self.course_coreq.append(course_coreq)

    self.requires_senior_standing = requires_senior_standing
    self.requires_dept_approval = requires_dept_approval

  """
  Setters

  """

  def setCourseId(self, course_id):
    self.course_id = course_id

  def setCourseName(self, course_name):
    self.course_name = course_name

  def setCredits(self, credits):
    self.credits = credits

  def setSugSemester(self, sugg_semester):
    self.sugg_semester

  def setTaken(self, taken):
    self.taken = taken

  def setGradeEarned(self, grade):
    self.earned_grade = grade

  def addCoursePreReq(self, prereq):
    self.course_prereq.append(prereq)

  def addCourseCoReq(self, coreq):
    self.course_coreq.append(coreq)

  def setReqSeniorStanding(self, does_it):
    self.requires_senior_standing = does_it

  def setReqDeptApproval(self, does_it):
    self.requires_dept_approval

  """
  Getters

  """

  def returnCourseId(self):
    return self.course_id

  def returnCourseName(self):
    return self.course_name

  def returnCredits(self):
    return self.credits

  def returnSugSemester(self):
    return self.sugg_semester

  def returnTaken(self):
    return self.taken

  def returnGradeEarned(self):
    return self.earned_grade

  def returnCoursePrereqs(self):
    return self.course_prereq

  def returnCourseCoreqs(self):
    return self.course_coreq

  def returnReqSeniorStanding(self):
    return self.requires_senior_standing

  def returnReqDeptApproval(self):
    return self.requires_dept_approval

  """
  Simple print Class object methods

  """
  def printCourse(self):
    print("Course ID: " + self.course_id, end=" ")
    print("Course Name: " + self.course_name)
    print("Credits: " + self.credits, end=" ")
    print("Semester: ", end="")
    print(self.sugg_semester)
    if (self.taken):
      if (self.earned_grade != None
          and self.earned_grade != "W"):
        print("Course Completed with a final grade of ", end="")
        print(self.earned_grade)
      elif (self.earned_grade == "W"):
        print("Withdrew from course")
      else:
        print("Course is in progress")
    else:
      print("Course not attempted")
    print()

  def printCoursePrereqs(self):
    print(self.course_prereq)

  def printCourseCoreqs(self):
    print(self.course_coreq)
