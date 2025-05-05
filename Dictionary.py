Students = {"name" : "Marks",
            "Alice" : 85,
            "Aarti" : 71,
            "Ritika": 90 }

student_name = input("Enter the student's name:")

if student_name in Students:
    print(f"{student_name}'s marks : {Students[student_name]}")
else:
    print(f"{student_name} not found in the record")
