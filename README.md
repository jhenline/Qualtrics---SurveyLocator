# Overview
Simple python script will take a survey id (e.g. SV_123ABC) from the user and resolve the name of the survey and the survey owner. Note: Qualtrics doesn't allow brand admins to view surveys they don't own or are collaborators of via the API. 

So, this tool is only helpful if you are a collaborator or member of a group that has access to the survey.

## Typical Use case
As a Brand Admin, you are given a URL to a survey and asked to locate the owner and name of the survey. While the admin interface allows you to search by Survey ID, it doesn't provide the name of the survey. This tool will identify the name of the survey if you belong to the group or were invited as a collab. If not, the only way to find the name of the survey is to generate and download a CSV of all surveys. 

## Example Contents of Config.ini file
[Qualtrics]
api_token = abc123
base_url = https://iad1.qualtrics.com
