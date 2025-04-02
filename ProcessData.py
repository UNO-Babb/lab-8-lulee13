#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def makeID(first, last, num):
  while len(last) < 3: #making sure the last name is sufficiently long
    last += "x" #you can use += for strings, which I think is pretty cool
  studentID = str.lower(first[0] + last[0:3] + num [-3:]) #formatting it to be lowercase because i like it more that way
  return studentID

def makeMajorYear (major, year):
  if str.lower(year[0:2]) == "fr": #checking year and assigning the correct abreviation
    year = "FR"
  elif str.lower(year[0:2]) == "so":
    year = "SO"
  elif str.lower(year[0:2]) == "ju":
    year = "JR" 
  elif str.lower(year[0:2]) == "se":
    year = "SR"
  else:
    year = "ERROR"
  majorYear = str.upper(major[0:3]) + "-" + year
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for student in inFile:
    studentData = student.split(" ")
    firstName = studentData[0]
    lastName = studentData[1]
    idNum = studentData[3]
    year = studentData[5]
    major = studentData[6]
    studentID = makeID(firstName, lastName, idNum)
    majorYear = makeMajorYear(major,year)

    studentOutput = lastName + "," + firstName + "," + studentID + "," + majorYear + "\n"
    outFile.write(studentOutput)

   

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
