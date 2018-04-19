import requests

def search (access_token, organizationId, q, aq, cq, pipeline):
    payloads = {'access_token': access_token, 'organizationId': organizationId, 'q': q, 'cq': cq, 'aq': aq, 'pipeline': pipeline}
    r = requests.get('https://platform.cloud.coveo.com/rest/search/v2', params=payloads)
    return r.json()