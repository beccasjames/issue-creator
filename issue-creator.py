## `source github/bin/activate` will open github virtualenv
## using external library called github3.py
## run `pip install github3.py` to install github library onto virtualenv
## run `python Desktop/issue-creator.py` to point to this file's location and update file name if you changed it!
## tip: begin lines with `clear &&` to clear the output of the previous command and run command cleanly

import csv
import sys
import time
import github3

gh = github3.login(token="PERSONAL-ACCESS-TOKEN-TODO")
repo = gh.repository("ORG-NAME-TODO","REPO-NAME-TODO")

## authenticates your identity with github using a generated personal access token
##allows you to access a given repo, where first item in () == org name and second is the repo where you want to create issue

milestones = {}
for milestone in repo.iter_milestones():
    milestones[milestone.title] = milestone.number
## this bit creates a dictionary of all the milestones present in your repo and associates their titles with their integer in a key

with open('LOCATION/FILENAME-TODO.CSV') as f:
## include the location/name of your csv file within open()
## ensure that your csv includes only the data you want to pull in and create issues for (i.e. no headers!)
## Becca should include a programmatic option to remove unnecessary rows
    reader = csv.reader(f)
    for row in reader:
        print('Creating an issue titled: ' + row[1])
## this tells you what your program is doing in your terminal
        labels=row[3].split(",")
## this allows you to use a comma-separated list surrounded by quotes to create a list of labels
        issue = repo.create_issue(title=row[1],body=row[2],labels=labels,assignee=row[4],milestone=(milestones[row[5]] if row[5] else None))
## creates an issue with keyword arguments that map to the title, body, labels, assignee, and milestone of the issue
## milestones should be represented by the string title of the milestone in your .csv file (see lines 18-20
## there is no support yet for multiple assignees (see github3.py bug #626)
        time.sleep(0.25)
## throttles the program so github continues to think you're awesome
