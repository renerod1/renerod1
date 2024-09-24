import configparser
import os

# Load the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the environment variable
github_user_name = 'renerod1'
gif_frame_duration = '7500'
generate_merged_prs = true

# Override the variable in the config file
config.set('Settings', 'gif_frame_duration', gif_frame_duration)
config.set('Settings', 'github_user_name', github_user_name)
config.set('Readme', 'generate_merged_prs', generate_merged_prs)

# Write the changes back to the config.ini file
with open('config.ini', 'w') as configfile:
    config.write(configfile)