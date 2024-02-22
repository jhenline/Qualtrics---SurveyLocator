import requests
import configparser

def get_survey_details(api_token, base_url, survey_id):
    endpoint = f'/API/v3/surveys/{survey_id}'
    headers = {'X-API-TOKEN': api_token}
    response = requests.get(base_url + endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching survey details:", response.status_code)
        return None

def get_owner_details(api_token, base_url, owner_id):
    user_endpoint = f'/API/v3/users/{owner_id}'
    headers = {'X-API-TOKEN': api_token}
    response = requests.get(base_url + user_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching user details:", response.status_code)
        return None

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')

api_token = config['Qualtrics']['api_token']
base_url = config['Qualtrics']['base_url']

# Prompt user to enter the survey ID
survey_id = input("Enter the survey ID (e.g., SV_123ABC): ")

# Fetch survey details
survey_details = get_survey_details(api_token, base_url, survey_id)
if survey_details:
    print("Survey Name:", survey_details['result']['name'])
    owner_id = survey_details['result']['ownerId']
    print("Survey Owner ID:", owner_id)

    # Fetch owner details
    owner_details = get_owner_details(api_token, base_url, owner_id)
    if owner_details:
        owner_name = owner_details['result']['firstName'] + " " + owner_details['result']['lastName']
        owner_email = owner_details['result']['email']
        print("Owner Name:", owner_name)
        print("Owner Email:", owner_email)