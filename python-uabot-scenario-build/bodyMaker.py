import json

'''
searchendpoint: string 
analyticsendpoint: string
orgName: string
randomGoodQueries: list os sting []
allowAnonymousVisits: bool
anonymousThreshold: int in seconds
timeBetweenVisits: int in seconds
timeBetweenActions: int in seconds
defaultPageViewField: string -> "fid28306"
randomCustomData: list of object
    Ex:
            {
                "apiname": "c_context_profile_Retail_Persona",
                "values": ["Celine the Photographer"]
            },
            {
                "apiname": "c_isbot", "values": ["true"]
            }

'''
def createBody(searchendpoint, analyticsendpoint, orgName, 
    randomGoodQueries, allowAnonymousVisits,
    anonymousThreshold, timeBetweenVisits, timeBetweenActions, defaultPageViewField,
    randomCustomData, globalFilter):
    return json.dumps({
    "searchendpoint" : searchendpoint,
	"analyticsendpoint" : analyticsendpoint,
	"orgName" : orgName,
	"randomGoodQueries": randomGoodQueries,
	"allowAnonymousVisits": allowAnonymousVisits,
	"anonymousThreshold" : anonymousThreshold,
	"timeBetweenVisits": timeBetweenVisits,
	"timeBetweenActions": timeBetweenActions,
	"defaultPageViewField":defaultPageViewField,
	"randomCustomData": randomCustomData,
	"globalFilter": globalFilter
    })