# issue-creator
A bulk ticket creator for Github issues! Create a bunch of issues all at one with one Python script and one .csv file.

Python script requires pointing to a .csv. This .csv file should have extraneous header rows removed (see `sample-issues.csv`)

Python script will create issue pulling in from 

To use script, update the following in the file:
  1) Your personal access token from Github
  2) The organization that your target repository lives in
  3) The repository to which you're intending to add issues
  4) The location and file name of your .csv (in a format like `sample-issues.csv`)

There is not currently support for adding assignees and milestones to your issues.
