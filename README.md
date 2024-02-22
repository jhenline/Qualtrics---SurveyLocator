Simple python script will take a survey id (e.g. SV_123ABC) from the user 
and resolve the name of the survey and the survey owner. Note: Qualtrics doesn't allow
brand admins to view surveys they don't own or are collaborators of via the API. 

So, this tool is only helpful if you are a collaborator or member of a group that has access to the survey.

##### Example Contents of Config.ini file #####
[Qualtrics]
api_token = abc123
base_url = https://iad1.qualtrics.com
