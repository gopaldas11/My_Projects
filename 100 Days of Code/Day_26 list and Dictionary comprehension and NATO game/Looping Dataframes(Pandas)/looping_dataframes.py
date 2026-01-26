import pandas
student_data = {
    "names": [ "Gopal", "Niloy"],
    "grades": [88,98]
}

student_dataframe = pandas.DataFrame(student_data)

for(index, row) in student_dataframe.iterrows():
    if row.names == "Gopal":
        print(row.grades)



#print(row.names)

