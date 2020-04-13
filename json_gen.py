import json

data = {}
data['app'] = []
data['app'].append({
    'app_name':"YOURAPPNAME",
    'app_version': '001',
    'askid': 'UHGWM110-XXXXXXXX',
    'logger_level': 'ERROR',
    'logger_path': 'default',
    'environment': 'development',
    'business_unit': 'YOURBUNAMEGOESHERE',
    'app_lang': 'PROGRAMLANGUAGE',
    'app_pools': 'IFYOUKNOWTHEM',
    'sub_app_name': '',
    'contrast_group': 'NAMEOFYOURGROUPFORCONTRAST',

})


with open('GIVETHISANAME.json', 'w') as outfile:
    json.dump(data, outfile)
