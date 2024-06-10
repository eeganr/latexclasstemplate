import os
import shutil

class_id = "ECON440_24"
short_id = "ECON"

num = input("Enter HW number: ")

filename = f"{short_id}_HW{num}"

os.mkdir(f"./{class_id}/{filename}")

shutil.copyfile(f"./{class_id}/{short_id}_HW_TEMPLATE/{short_id}_HW_X.tex", f"./{class_id}/{filename}/{filename}.tex")

filename = f"./{class_id}/{filename}/{filename}.tex"

with open(filename) as f:
    global s
    s = f.read()

with open(filename, 'w') as f:
    s = s.replace('X', num)
    f.write(s)