import configparser
import os

# Load the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the environment variable for the GitHub username
github_user_name = 'codingwithstrangers'
gif_frame_duration = '10000'
generate_merged_prs = 'true'

# Update the github_user_name in the config file
# this pertains to the setting 
config.set('Settings', 'github_user_name', github_user_name)
config.set('Readme', 'generate_merged_prs', generate_merged_prs)
config.set('Settings', 'gif_frame_duration', gif_frame_duration) #the readme is for this line the spacing matters for the operation

# Write the changes back to the config.ini file
with open('config.ini', 'w') as configfile:
    config.write(configfile)