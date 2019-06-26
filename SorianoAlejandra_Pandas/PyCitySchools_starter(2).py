
import pandas as pd
import numpy as np

school_data = "Resources/schools_complete.csv"
student_data = "Resources/students_complete.csv"


school_data = pd.read_csv(school_data)
student_data = pd.read_csv(student_data)


school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])





total_schools = school_data["School ID"].count()
total_schools




total_students = student_data["Student ID"].count()
total_students




total_budget = school_data["budget"].sum()
total_budget


average_math = student_data["math_score"].mean()
average_math


average_reading = student_data["reading_score"].mean()
average_reading




average_score = (average_reading + average_math) /2
average_score



passing_math = student_data.loc[student_data["math_score"] >= 70, [
    "math_score"]]
passing_math.head()



passing_reading = student_data.loc[student_data["reading_score"] >= 70, [
    "reading_score"]]
passing_reading.head()



percentage_math= ((passing_math["math_score"].count())/total_students)*100
percentage_math



percentage_reading= ((passing_reading["reading_score"].count())/total_students)*100
percentage_reading



stats_df = pd.DataFrame({
    "Total Schools": [total_schools],
    "Total Students": [total_students],
    "Total Budget $": [total_budget],
    "Average Math Score":[average_math],
    "Average Reading Score": [average_reading],
    "% Passing Math": [percentage_math],
    "% Passing Reading": [percentage_reading],
    "% Overall Passing Rate": [average_score]
})
stats_df





perstudent = (school_data["budget"])/(school_data["size"])
school_data["Per Student Budget"] = perstudent
school_data.head()




average_grades = student_data[["school_name", "reading_score", "math_score"]]
average_grades.head()




school_group = average_grades.groupby(["school_name"])
average_school = school_group.mean()
average_school.head()



student_70_math = ((student_data["math_score"] >= 70).groupby(student_data.school_name).sum())
student_70_math


student_70_reading = ((student_data["reading_score"] >= 70).groupby(student_data.school_name).sum())
student_70_reading














