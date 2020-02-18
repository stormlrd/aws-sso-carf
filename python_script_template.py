#######################################################################
# Name: aws-sso-carf
# Version:  0.01
# Author: Paul Dunlop
# Description:
#   skeleton python script that allows for cross account looping in
#   AWS where AWS SSO is used to federate access
#######################################################################

###################################
# Library Work
#--------------
# import AWS Python SDK
import boto3
# for folder testing import os library
import os
# for clear() import only system from os 
from os import system, name 

# get pathlib class from path library for use with home folder on all OSes
from pathlib import Path
#JSON library for the sso cached cred files
import json

###################################
# Setup variables
#--------------
version="0.01" # used in console output
home = str(Path.home()) # find the current users home folder on all OSes to get to .aws folder

###################################
# FUNCTIONS
###################################
#----------------------------------
# Function: clear()
# Purpose: clears the screen
# Arguments: None
#----------------------------------
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#----------------------------------
# Function: aws_calls()
# Purpose: your code to run in aws per account. modify as you see fit
# Arguments: None but modify as you see fit
#----------------------------------
def aws_calls():
    #### YOU CODE GOES HERE###

    #Setup client
    #If your AWS SSO credentials are valid, the AWS CLI uses them to securely retrieve
    #AWS temporary credentials for the IAM role specified in the profile.
    #session = boto3.session.Session(profile_name='primary')
    #client = session.client('sso')
    client = boto3.client('sso')

    # get list of all accounts
    response = client.list_accounts(
        maxResults=123,
        accessToken=accessTokenfound
    )
    print("response: ", response)

    # for each account get a list of unique roles & create a unique list of roles that are found in every account

    # display list of roles found in every account

    # loop thru each account and assume the role
    response = client.get_role_credentials(
        roleName='AdministratorAccess',
        accountId='387383504163',
        accessToken=accessTokenfound
    )
    print("response: ", response)

########################
# MAIN ROUTINE
########################
clear()
# print banner
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("aws-sso-carf v", version)
print("Author: Paul Dunlop")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Check for cached creds folder
aws_sso_cache_folder = os.path.join(home,".aws","sso","cache")
test = os.path.isdir(aws_sso_cache_folder)
if test:
    print("Found cached credentials folder.")
else:
    print("An aws cli sso folder was not found in your  .aws folder. please ensure you have configured and logged into aws sso before using.")
    exit()

# there should only be two files in this folder.
# so get the one thats not botocore-client-id-[region].json
found_flag = False
file_list = os.listdir(aws_sso_cache_folder)
for file in file_list:
    if file[0:18]== "botocore-client-id":
        pass
    else:
        cached_credentials_filename = file
        found_flag = True

# if a file is found then read in the accessToken from it else bomb out
if found_flag:
    # we've got a file to open
    print("Found cached credentials file of: ", cached_credentials_filename)
    file_to_read = os.path.join(aws_sso_cache_folder, cached_credentials_filename)
    with open(file_to_read, 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    # do a check here for the expiration of the token or not. if not expired then read it and let the app work.
    expired_token = False # hardset flag for now
    accessTokenfound=str(obj['accessToken'])
else:
    #we've got no file to open! :(
    print("No cached credentials file found. Please ensure you use aws sso login --profile primary to login")
    exit()

if expired_token: # true = expired, must re-login
    print("Token has expired. Please use aws sso login --profile primary again.")
    exit()
else: # false = non expired, current session available to use
    print("Valid token found. Running cross account loop and API calls.")
    main_routine()