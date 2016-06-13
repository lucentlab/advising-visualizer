import sys
from student import Student

print("Start driver")

# (Required) Create an instance of student
p = Student("CS")
 
# (Optional)
#p.setMajor("CHM")

# (Optional) Returning the Student's Major
print("Major set to " + p.returnMajor())

# (Optional) Lets the parser know which classes matter for major.
#   If the Major is set, as above, this will be done automatically. 
#   This is legacy code, useful for testing new variations of Major requirements
#p.defineMajorReqs("DATA/required_PHY_courses.csv")
#p.defineMajorReqs()

# (Required) Parse text transcript for any classes
#   Class defined as two or three letters, followed by two or three spaces,
#   and then two or three numbers.
p.parseTranscript("DATA/jesse_unofficial_transcript.txt")

# (Required) Compare the Major requirements to the parsed transcript
p.compareMajorToTranscript()

# (Optional) Prints out Major Requirements in a Block Format
p.printMajorReqs()

print("")
print("-----")
print("")

# (Optional) Prints out all classes in the transcript
p.printCourses()

print("")
print("-----")
print("")

print("End driver")
