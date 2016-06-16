#!/usr/bin/python
#    _                       _       _        _   
#   / / _   _  ___ ___ _ __ | |_    / /  __ _| |__
#  / / | | | |/ __/ _ \ '_ \| __|  / /  / _` | '_ \ 
# / /___ |_| | (__  __/ | | | |_  / /___ (_| | |_) |
# \____/\__,_|\___\___|_| |_|\__| \____/\__,_|_.__/
#
#
# Dependancies
#
# Author: Jesse Goble
# 2016
#
# Usage pseudocode
#
# Imports
from __future__ import print_function
import sys, math
from optparse import OptionParser
from Tkinter import *
from student import Student

__author__  = "Jesse Goble"
__version__ = "1.0"

# Set constants
GOOD_COLOR_1 = "#0CEB13"
GOOD_COLOR_2 = "#8CF59A"
NEUTRAL_COLOR_1 = "#CFD4D0"
NEUTRAL_COLOR_2 = "#C0C0C0"
WARNING_COLOR_1 = "#E8E413"
WARNING_COLOR_2 = "#C4BA27"
BAD_COLOR_1 = "#F00A0A"
BAD_COLOR_2 = "#960606"
GRADE_THRESHOLD = 2.0

# Initialize Variables
start_x = 10  
start_y = 10 

box_height = 100
stop_y = 100
box_width = 220
stop_x = 220 
last_sem = 0

count = 0
col = 1
limit = 9

# Functions
def checkRequiredArguments(opts, parser):
    missing_options = []
    for option in parser.option_list:
        if (re.match(r'^\(REQUIRED\)', option.help)
                and eval('opts.' + option.dest) == None):
            missing_options.extend(option._long_opts)
        if (len(missing_options) > 0):
            parser.error('Missing REQUIRED parameters: ' + str(missing_options))

def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def onLeftClick(event):
    print('Got left mouse button click: ', end=' ')
    showPosEvent(event)
    print(event.widget.find_closest(event.x, event.y))

# Create Command-line option parser.
parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
# Add option for -v or --view which shows a specific Major's suggested flow.
parser.add_option("-v", "--view", action="store", type="string", dest="view",
            help="(OPTIONAL) Specify a Major, using the two or three letter designation, to display. By default, no major is specified and a complete list of completed/in progress courses will be displayed.")
# Add option for -f or --file, which allows for the filename of the student's
# transcript text file
parser.add_option("-f", "--file", action="store", type="string",
            dest="student_file",
            help="(REQUIRED) Specify the relative path and filename for the student's transcript text file.")

(options, args) = parser.parse_args()
checkRequiredArguments(options, parser)

# Create Tk object.
master = Tk()

# Make a canvas.
w = Canvas(master, width=1800, height=800)
w.grid(column=0, row=0, sticky=N+S+E+W)

master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)

vbar=Scrollbar(master, orient=VERTICAL)
vbar.grid(row=0, column=1, sticky=N+S)
w.config(yscrollcommand=vbar.set)
vbar.config(command=w.yview)

hbar=Scrollbar(master, orient=HORIZONTAL)
hbar.grid(row=1, column=0, stick=E+W)
w.config(xscrollcommand=hbar.set)
hbar.config(command=w.xview)

w.bind('<Button-1>', onLeftClick)
#w.pack(side=LEFT, expand=True, fill=BOTH)

# Create student object.
p = Student(options.view)
p.parseTranscript(options.student_file)
p.compareMajorToTranscript()

course_list = []
if options.view:
    course_list = p.returnMajorReqs()
else:
    course_list = p.returnCourses()

for course in course_list:
    if (course.returnSugSemester() != last_sem
            or (not options.view and count > limit)):
        start_x = (box_width + 10)
        start_x *= int(last_sem) if (options.view) else col
        start_y = 10
        stop_x  = start_x + 220
        stop_y  = 100
        count   = 0
        col     += 1
    last_sem = course.returnSugSemester()

    text_string = course.returnCourseId() + "\n"
    text_string += str(course.returnCourseName())[0:27]
    text_string += "\n"

    fill_color = None
    active_fill = None

    if (course.returnTaken() and course.returnGradeEarned() != "W"
            and course.returnGradeEarned() != "TR"
            and course.returnGradeEarned() != "P"):
        if float(course.returnGradeEarned()) >= float(GRADE_THRESHOLD):
            fill_color = GOOD_COLOR_1
            active_fill = GOOD_COLOR_2
        else:
            fill_color = BAD_COLOR_1
            active_fill = BAD_COLOR_2
    elif course.returnGradeEarned() == "TR":
        fill_color = NEUTRAL_COLOR_1
        active_fill = NEUTRAL_COLOR_2
    elif course.returnGradeEarned() == "W":
        fill_color = WARNING_COLOR_1
        active_fill = WARNING_COLOR_2
    elif course.returnGradeEarned() == "P":
        fill_color = GOOD_COLOR_1
        active_fill = GOOD_COLOR_2
    else:
        fill_color = None
        active_fill = None

    w.create_rectangle(start_x, start_y, stop_x, stop_y, dash=(4,4),
                        fill=fill_color, activefill = active_fill,
                        tags=course.returnCourseName())

    if course.returnGradeEarned() is not None:
        text_string += str(course.returnGradeEarned()) + "\n"
    else:
        text_string += "Course Not Taken\n"

    text_string += str(course.returnSugSemester())

    w.create_text(start_x + 10, start_y + 10, anchor=NW, text=text_string)

    start_y += 100
    stop_y  += 100
    count   += 1

w.create_window((0,0), anchor=NW)
w.update_idletasks()
w.config(scrollregion = w.bbox("all") )

for child in w.children.values():
    print(child)
master.mainloop()
