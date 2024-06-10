import os
import shutil
from datetime import date, datetime
import subprocess

your_schedule = "quarter" # replace with "semester" if you're on a semester system
github_username = "eeganr"
github_actions = True # Change to false if you wanna do this manually

# ----------------

notes_folder = os.path.dirname(os.getcwd())

def get_suggested_name():
    Y = 2024 # dummy leap year to allow input X-02-29 (leap day)

    if your_schedule == "quarter":
        # based roughly on stanford
        seasons = [('Win', (date(Y, 1, 1), date(Y, 2, 25))),
            ('Spr', (date(Y, 2, 26), date(Y, 6, 1))),
            ('Sum', (date(Y, 6, 2), date(Y, 8, 30))),
            ('Aut', (date(Y, 8, 31), date(Y, 11, 20))),
            ('Win', (date(Y, 11, 21), date(Y, 12, 31)))]
    elif your_schedule == "semester":
        # based roughly on stanford
        seasons = [('Spr', (date(Y, 1, 1), date(Y, 5, 1))),
            ('Sum', (date(Y, 5, 2), date(Y, 8, 1))),
            ('Aut', (date(Y, 8, 1), date(Y, 12, 31)))]


    def get_season(now):
        if isinstance(now, datetime):
            now = now.date()
        now = now.replace(year=Y)
        return next(season for season, (start, end) in seasons
                    if start <= now <= end)

    season = get_season(date.today())
    year = date.today().year
    name = f"{year%100}{season}Notes"
    return name


namesuggest = get_suggested_name()

while True:
    parent = input(f"Enter folder name or type y to accept suggestion ({namesuggest}): ")

    if parent == "y": 
        parent = namesuggest
        break
    else: 
        conf = input(f"Confirm custom directory name ({parent})? (y/n): ")
        if conf == "y":
            break

folder = f"{notes_folder}/{parent}"
dir_check = os.path.exists(folder)

if not dir_check:
    print("Directory not detected, creating now")
    os.mkdir(folder)
    shutil.copyfile("commit.sh", f"{folder}/commit.sh")
    shutil.copyfile(".flake8", f"{folder}/.flake8")
    shutil.copyfile(".gitignore", f"{folder}/.gitignore")
    shutil.copyfile("eeganlatex.sty", f"{folder}/eeganlatex.sty")
    shutil.copyfile("template.md", f"{folder}/README.md")
    with open(f"{folder}/README.md") as f:
        global s
        s = f.read()
    with open(f"{folder}/README.md", 'w') as f:
        s = s.replace('name', parent)
        f.write(s)
    command = 'git init; git add .; git commit -m "initialized"'
    ret = subprocess.run(command, shell=True, cwd=folder)
    if github_actions:
        # command = f'git remote add origin git@github.com:{github_username}/{parent}.git; git push -u origin main'
        ret = subprocess.run(command, shell=True)
    
else:
    print("Directory detected")

# class_id = input("Enter class ID (e.g. STATS116)")
# short_id = input("Enter short ID (e.g. STATS)")