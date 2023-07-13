## Daily actions workflow

This workflow is triggered by a daily cron job. It will run by the following actions:
- [x] Commit and push the changes to the repository
- [x] Create a pull request to merge the changes into the master branch

if a commit is observed in the 24 hours, the tests will not be run
