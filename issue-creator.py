## `source github/bin/activate` will open github virtualenv
## using external library called github3.py
## run `pip install github3.py` to install github library onto virtualenv
## run `python Desktop/github_issues.py` to point to file location
## begin with `clear &&` to clear the output of the previous command and run command cleanly

import csv
import time
import github3

gh = github3.login(token="PERSONAL-ACCESS-TOKEN-TODO")
repo = gh.repository("ORG-NAME-TODO"),"REPO-NAME-TODO")

## authenticates your identity with github using a generated personal access token
##allows you to access a given repo, where first item in () == org name and second is the repo where you want to create issue

with open('LOCATION/FILENAME.CSV-TODO') as f:
## include the location/name of your csv file within open()
## ensure that your csv includes only the data you want to pull in and create issues for (i.e. no headers!)
## Becca should include a programmatic option to remove unnecessary rows
    reader = csv.reader(f)
    for row in reader:
        print ('Creating an issue for ' + row[0])
## this tells you what your program is doing in your terminal
        labels=[]
        labels.append(row[2])
## this creates a list called labels, getting around the problem that labels need to be arrays of strings...
## this still can't handle multiple labels though :/
        issue = repo.create_issue(title=row[0],body=row[1],labels=labels)
## creates an issue with keyword arguments that map to the title, body, and labels of the issue
## there is no support here for assignees or milestones yet
        time.sleep(1)
## throttles the program so github continues to think you're awesome
