import json
import requests

def readJson(file_path):
    return json.load(open(file_path))

def getFacetValue (access_token, organizationId, field):
    payloads = {'access_token': access_token, 'organizationId': organizationId, 'field': field, 'maximumNumberOfValues': 100}
    r = requests.get('https://platform.cloud.coveo.com/rest/search/v2/values', params=payloads)
    return r.json()

def createJsonFile(file_path, json):
    with open(file_path, 'w') as f:
        f.write(json)

config = readJson('config.json')


tab_listing = config['tabNames']

facet_listing = config['facetNames']

for facet in facet_listing:
    facet_values = getFacetValue (config['access_token'], config['organizationId'], facet_listing[facet]['facetField'])

    value_list = []

    for values in facet_values['values']:
        value_list.append(values['value'])

    test = facet_listing[facet]['facetValues']

    facet_listing[facet]['facetValues'] = value_list

    print (test)

    


createJsonFile('facet.json', json.dumps(facet_listing))
createJsonFile('tab.json', json.dumps(tab_listing ))