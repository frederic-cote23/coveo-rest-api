import requests

def search (access_token, organizationId, aq, q, pipeline):
    payloads = {'access_token': access_token, 'organizationId': organizationId, 'aq': aq, 'q': q, 'pipeline': pipeline}
    r = requests.get('https://platform.cloud.coveo.com/rest/search/v2', params=payloads)
    return r.json()