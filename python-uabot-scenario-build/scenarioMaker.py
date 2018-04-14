import json

'''
    				{
					"type" : "SetOrigin", 
					"arguments" : {
						"originLevel1" : "CoveoSearch",
						"originLevel2" : "default",
						"originLevel3" : "http://retail.coveodemo.com/"
					}
				},
'''

def event_SetOrigin(originLevel1, originLevel2, originLevel3):
    return json.dumps( {
        "type": "SetOrigin", 
        "argument": {
            "originLevel1" : originLevel1,
            "originLevel2" : originLevel2,
            "originLevel3" : originLevel3
            } 
        })

def event_SetReferrer(SetReferrer, referrer):
    return json.dumps({
        "type" : SetReferrer, 
        "arguments" : {
            "referrer" : referrer
        }
    })

def event_RandomSearch():
    return json.dumps({
					"type": "Search",
					"arguments": {
						"queryText": "",
						"goodQuery": True
					}
				})