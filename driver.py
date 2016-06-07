from student import Student

print("Start driver")

# (Required)
p = Student()
 
# (Optional)
p.setMajor("PHY")

# Checking to see if Major was set
print("Major set to " + p.returnMajor())

# (Required) Lets the parser know which classes matter for major.
#p.defineMajorReqs("DATA/required_PHY_courses.csv")
p.defineMajorReqs()

# (Optional) Prints out Major Requirements in a Block Format
#p.printMajorReqs()

# (Required) Processes the txt version of the transcript.
#p.processTranscript("DATA/jesse_unofficial_transcript.txt")

# (Optional) Parse text transcript for any classes
#   Class defined as two or three letters, followed by two or three spaces,
#   and then two or three numbers.
p.parseTranscript("DATA/jesse_unofficial_transcript.txt")

# (Optional)
#p.printTranscript()
p.printCourses()

print("End driver")
