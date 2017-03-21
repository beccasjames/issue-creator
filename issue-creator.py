## Pointing to the parent directory of this file, in your terminal run `virtualenv issue-creator`
## Activate the virtualenv by running `source issue-creator/bin/activate`
## Run `pip install github3.py` to install github3.py library in virtualenv
## Run `python issue-creator.py` to execute this script

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
## this creates a dictionary of all the milestones present in your repo and associates their titles with their integer in a key

with open('LOCATION/FILENAME-TODO.CSV') as f:
## include the location/name of your csv file within open()
## ensure that your csv includes only the data you want to pull in and create issues for (i.e. no spreadsheet column/row headers!)
    reader = csv.reader(f)
    for row in reader:
        print('Creating an issue titled: ' + row[1])
## this allows you to see what your computer is working on when this script runs through your terminal
        labels=row[3].split(",")
## this allows you to use a comma-separated list surrounded by quotes to create a list of labels
        issue = repo.create_issue(title=row[1],body=row[2],labels=labels,assignee=row[4],milestone=(milestones[row[5]] if row[5] else None))
## creates an issue with keyword arguments that map to the title, body, labels, assignee, and milestone of the issue
## milestones should be represented by the string title of the milestone in your .csv file (see lines 18-20
## there is no support yet for multiple assignees (see github3.py bug #626)
        time.sleep(0.25)
## throttles the program so github continues to think you're awesome
