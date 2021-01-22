import csv
import string
from connection import *
import random
from datetime import datetime
import time

def hfragment():
    cur = conn.cursor()
    cur.execute("CREATE table Employee3 AS SELECT * FROM Employee WHERE Gender = 'M'")
    cur.execute("CREATE table Employee4 AS SELECT * FROM Employee WHERE Gender = 'F'")
    conn.commit()
    cur.close()

def vfragment():
    cur = conn.cursor()
    cur.execute("CREATE table Employee5 AS SELECT Employee_ID,First_Name,Gender FROM Employee")
    cur.execute("CREATE table Employee6 AS SELECT Employee_ID,Last_name FROM Employee")
    conn.commit()
    cur.close()

def hybridfragment():
    cur= conn.cursor()
    cur.execute("CREATE table Employee7 AS SELECT * FROM Employee5 WHERE Gender='F' ")
    conn.commit()
    cur.close()
