import os
import shutil
from datetime import date

class_id = "ECON440_24"
short_id = "ECON"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_abbreviations = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

today = str(date.today())

month = months[int(today[5:7]) - 1]
month_abbr = month_abbreviations[int(today[5:7]) - 1]
day = str(int(today[8:]))

filename = f"{short_id}_{today[5:]}"

os.mkdir(f"./{class_id}/{filename}")

shutil.copyfile(f"./{class_id}/{short_id}_NOTES_TEMPLATE/{short_id}_M-DD.tex", f"./{class_id}/{filename}/{filename}.tex")

filename = f"./{class_id}/{filename}/{filename}.tex"

with open(filename) as f:
    global s
    s = f.read()

with open(filename, 'w') as f:
    s = s.replace('MMMMMMM', month)
    s = s.replace('MMM', month_abbr)
    s = s.replace('X', day)
    f.write(s)