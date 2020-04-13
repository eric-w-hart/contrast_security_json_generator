# Import modules required to pull from Excel, OrderedDict and json
# These are required to ingest the data for the key value pairs
# This script was built to support yaml creation for onboarding
# PEDS applications within Contrast Assess.
#
# This presupposes development teams have adopted the Jenkins Pipeline as Code
# and are using the Global Pipeline Library from Optum Github.
# Author Eric Hart
# Architect
# PEDS Security

import xlrd

from collections import OrderedDict

import json

# Open the Excel workbook then select the first worksheet
workbook = xlrd.open_workbook('USEYOUREXCELHERE.xlsx')
sheet = workbook.sheet_by_index(0)

# Build the list to hold the application data

apps_list =[]

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sheet.nrows):
    apps = OrderedDict()
    row_values = sheet.row_values(rownum)
    apps['app_name'] = row_values[0]
    apps['askid'] = row_values[1]
    apps['logger_level'] = row_values[2]
    apps['logger_path'] = row_values[3]
    apps['environment'] = row_values[4]
    apps['business_unit'] = row_values[5]
    apps['app_lang'] = row_values[6]
    apps['app_pools'] = row_values[7]
    apps['sub_app_name'] = row_values[8]
    apps['contrast_group'] = row_values[9]


    apps_list.append(apps)

# Serialize the list of dicts to JSON
jdump = json.dumps(apps_list)

# Create a json file, open it then write to file
with open('GIVEYOURFILEANAME.json', 'w') as filedump:
    filedump.write(jdump)











