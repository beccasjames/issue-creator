# issue-creator
A bulk ticket creator for GitHub issues! Create a bunch of issues all at once with one Python script and one .csv file.

Python script requires pointing to a .csv. This .csv file should have extraneous header rows removed (see `sample-issues.csv`)

## To use script, update the following in the file:

  1) Your personal access token from GitHub
  
  2) The organization that your target repository lives in
  
  3) The repository to which you're intending to add issues
  
  4) The location and file name of your .csv (in a format like `sample-issues.csv`)

## Notes

1) This script relies on an external library called [github3.py](https://github3py.readthedocs.io/en/master/). There is no support for adding multiple assignees yet :(
