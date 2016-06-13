#!/usr/bin/python

from optparse import OptionParser
from Tkinter import *
from student import Student

view = None

parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
parser.add_option("-v", "--view", action="store", type="string", dest="view",
			help="(Optional) Specify a Major, using the two or three letter designation, to display. By default, no major is specified and a complete list of completed/in progress courses will be displayed.")
(options, args) = parser.parse_args()

master = Tk()

w = Canvas(master, width=1200, height=1000)
w.pack()

p = Student(options.view)

if options.view:
	print("Major specified")
	p.defineMajorReqs("DATA/required_" + p.returnMajor() + "_courses.csv")
	p.processMajorReqs("DATA/required_" + p.returnMajor() + "_courses.csv")

p.parseTranscript("DATA/jesse_unofficial_transcript.txt")

start_x = 10
start_y = 10

box_height = 100
box_width = 220 
last_sem = 0

if not options.view:
	print("No Major selected")
else:
	print("Major is " + p.returnMajor())

#for course in p.returnCourses():
for course in p.returnMajorReqs():
	if (course.returnSugSemester() != last_sem):
		start_x = (box_width + 10) * last_sem
		start_y = 10
	last_sem = course.returnSugSemester()
	w.create_rectangle(start_x, start_y, box_width, box_height, dash=(4,4))
	w.create_text(start_x+13, start_y+10, anchor=NW, text=course.returnCourseId() + "\n" + course.returnCourseName() + "\n" + course.returnGradeEarned() + "\n")
	start_y += 100
	box_height += 100
	course.returnCourseId()
mainloop()
