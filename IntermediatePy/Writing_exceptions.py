import csv

#create an empty list to save csv file to
data = []
path = "student_grades.csv"

#Making a customer error exceptor in python
class StudentFailException(ValueError):
    pass

#open csv file and save to the existing data list
def OpenCSVandAppend(filePath):
    with open(filePath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)

#Goes through list and converts any string integers into integers
def IntegerConverter(data):
    for student in range(len(data)):
        for grade in range(len(data[student])):
            try:
                data[student][grade] = int(data[student][grade])
            except(ValueError):
                continue

#Calculates the average grade and designates either pass or fail
def GradeChecker(data):

    for i in range(1, len(data)):
        gradeAverage = sum(data[i][1:5]) / 4
        data[i].append(gradeAverage)
        if gradeAverage >= 70:
            data[i].append(True)
        else:
            data[i].append(False)

def PrintFunction(data):
    for i in range(1, len(data)):
        print(data[i][0], data[i][-2], end='')
        if data[i][-1]:
            raise StudentFailException("Fail")

if __name__ == "__main__":
    OpenCSVandAppend(path)
    IntegerConverter(data)
    GradeChecker(data)
    PrintFunction(data)