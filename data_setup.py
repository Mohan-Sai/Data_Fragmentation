import csv
import string
from connection import *



def insert_employee():
    cur = conn.cursor() 
    with open("emp_data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            cur.execute("insert into Employee (Employee_ID, First_Name, Last_Name, Gender, Email) values "
                        "(:1, :2, :3, :4, :5)",
                        (lines[0], lines[1], lines[2], lines[3],lines[4]))
    cur.close()
    conn.commit()

insert_employee()