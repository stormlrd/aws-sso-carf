# aws-sso-carf
AWS SSO Cross Account Roles Framework. A Python script baseline for simplifying hitting more than one account in an AWS SSO federated environment.

# Example Purpose
If you have setup AWS SSO and provisioned a baseline role into all accounts for read only
then you could use this script to conduct audits.

# Usage
- Clone this repository
- Copy the python_script_template.py to your own repository
- Add the appropriate API calls you're seeking to undertake per account into the code
- Set up aws cli v2 properly for your primary account
- Login to your primary account using aws sso login --profile=primary
- Execute your script
- Select role to use to cross account into all accounts
- Let script run

# Script Pre-Reqs
- You must have AWS SSO set up
- You must have an AWS role provisioned in AWS SSO
- You must have AWS CLI V2 installed & configured for your AWS SSO (you must have at least 1 role setup in your .aws/config file for the primary authentication to happen)
- You must have used aws sso login --profile=primary (or what ever you called the primary profile) before executing your script.

# Why do I have to aws sso login --profile=primary before executing the script?
Because the AWS CLI v2 and BOTO3 library require an initial token to be created that is used when assuming a role in a member account. So the first thing to do is to establish that primary token set using a role. It doesnt really matter which one you pick for your primary profile. You will need just one.