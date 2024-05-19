with open("students.csv")as f:
    for line in sorted(f):
        name ,house = line.rstrip().title().split(",")
        print(f"hello, {name} is in {house}")

import csv

name = input("what's your name? ")
house = input("what's your house name? ")

with open("students.csv","a")as f:
    writer = csv.DictWriter(f,fieldnames= ["name","house"])
    writer.writerow({"house":house,"name":name})

name = input("what's your name? ")
house = input("what's your house name? ")

with open("students.csv","a")as f:
    writer = csv.writer(f)
    writer.writerow([name,house])
students = []

with open ("students.csv")as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({"name":row["name"] , "house":row["house"]})

with open ("students.csv")as f:
    reader = csv.reader(f)
    for name, house in reader:
        students.append({"name":name , "house":house})

    for line in f:
        name, house = line.rstrip().title().split(",")
        student = {"name":name , "house":house}
        students.append(student)

for student in sorted(students,key=lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")

def get_name(student):
    return student["name"]

for student in sorted(students,key=get_name):
    print(f"{student['name']} is in {student['house']}")

