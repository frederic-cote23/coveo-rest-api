import json
import searchApi
import fileManager

config = fileManager.readJson('config.json')

q_list = fileManager.readDict(config['queryFile'])
facet_list = fileManager.readJson(config['facetFile'])
tab_list = fileManager.readJson(config['tabFile'])

result_list = {}

for q in q_list:

    result_list[q] = {}

    for tab in tab_list:
        tab_cq = tab_list[tab]['cq']
        tab_name = tab_list[tab]['name']
        result_list[q][tab] = { "cq": tab_cq, "facets": [] }
        
        for facet in facet_list:
            if( tab in facet_list[facet]['facetTab'] ):
                max_number_of_facet_values = config['maxNumberOfFacetToTest']
                for value in facet_list[facet]['facetValues'][0:max_number_of_facet_values]:
                    aq = facet_list[facet]['facetField']+"=="+value
                    facetField = facet_list[facet]['facetField']
                    facetTitle = facet_list[facet]['facetTitle']

                    query = searchApi.search(config['access_token'], config['organizationId'], q, aq, tab_cq, config['pipeline'])

                    result = {}

                    result['totalCount'] = query['totalCount']
                    result['documents'] = []
                    i = 0


                    for document in query['results']:
                        result['documents'].append(document['title'])
                        i+=1
                        if i >= 15 or  i > len(query['results']):
                            break
                    
                    result_list[q][tab]['facets'].append({"facetValue": aq, "facetField": facetField, "facetTitle": facetTitle, "searchResults": result})



with open(config['resultListFile'], 'w') as outfile:
    json.dump(result_list, outfile)




'''
                query = searchApi.search(config['access_token'], config['organizationId'], q, aq, tab_cq, config['pipeline'])

                result = {}
                result['aq'] = aq
                result['totalCount'] = query['totalCount']
                result['documents'] = []
                i = 0


                for document in query['results']:
                    result['documents'].append(document['title'])
                    i+=1
                    if i >= 15 or  i > len(query['results']):
                        break
                
                result_list[q][tab]['facets'][facet] = result 

with open(config['resultListFile'], 'w') as outfile:
    json.dump(result_list, outfile)

'''

'''
result_list
 {
     "[QUERY]": {
         "tabName": {
             "cq": [CQ],
            "facets":[
                {
                    "facetTitle": "[facetTitle]",
                    "facetField": "facetField",
                    "facetValues": [
                        {
                            "aq": "[AQ]",
                            totalCount: 0,
                            "documents": []
                        }
                    ]
                }
            ]

         }

     }

 }
'''



'''
for tab in tab_list:
    print('--------------'+tab+'--------------')
    tab_cq = tab_list[tab]['cq']
    tab_name = tab_list[tab]['name']
    result_list[tab] = {"tabName": tab_name, "tabCQ": tab_cq, "facet": {}}
    
    for facet in facet_list:
        print('--------------'+facet+'--------------')
        result_list[tab]['facet'][facet] = {}
        if( tab in facet_list[facet]['facetTab'] ):
            result_list[tab]['facet'][facet]['facetValues'] = facet_list[facet]['facetValues'][0:5]
            result_list[tab]['facet'][facet]['facetField'] = facet_list[facet]['facetField']
            result_list[tab]['facet'][facet]['facetTitle'] = facet_list[facet]['facetTitle']

            result_list[tab]['facet'][facet]['query'] = {}

            for value in facet_list[facet]['facetValues'][0:5]:
                aq = facet_list[facet]['facetField']+"=="+value
                for q in q_list:
                    print(tab+'-->'+aq+'-->'+q)
                    query = searchApi.search(config['access_token'], config['organizationId'], q, aq, tab_cq, config['pipeline'])

                    result = {}

                    result['totalCount'] = query['totalCount']
                    result['documents'] = []
                    i = 0


                    for document in query['results']:
                        result['documents'].append(document['title'])
                        i+=1
                        if i >= 15 or  i > len(query['results']):
                            break
                    
                    result_list[tab]['facet'][facet]['query'] = result 


with open(config['resultListFile'], 'w') as outfile:
    json.dump(result_list, outfile)
'''

'''
config_file = 'config.json'

config = fileManager.readConfig(config_file)

print(config)

access_token = 'xxcb8b6a78-16a2-4aec-b9a6-27df2ea0f5bc'
organizationId = 'coveolearningbasicanalytics'
aq = '@source="App Store"'
pipeline = 'default'

q = 'apple'
q_word_file = 'dic.text'
q_list = fileManager.readDict(q_word_file)

result_list_file = 'result_list.json'

scenario_file = 'scenario.json'

config_file = 'config.json'

config = fileManager.readConfig(config_file)

print(config)

scenario = bodyMaker.createBody(searchendpoint, analyticsendpoint, orgName, 
    randomGoodQueries, allowAnonymousVisits,
    anonymousThreshold, timeBetweenVisits, timeBetweenActions, defaultPageViewField,
    randomCustomData, globalFilter))

event1 = scenarioMaker.event_SetOrigin('o1', 'o2', 'o3')
event2 = scenarioMaker.event_RandomSearch()

scenario = {
	"searchendpoint" : "https://platform.cloud.coveo.com/rest/search/",
	"analyticsendpoint" : "https://usageanalytics.coveo.com/rest/v15/analytics/",
	"orgName"     : "sitecorecommercedemo",
	"randomGoodQueries": ["Mirrorless", "lens", "photos", "background blur", "professional sensor camera", "pro dslr", "16–50mm", "55mm", "18 megapixel", 
		"camera bag compartment", "zooming shaking distance", "nonslip tripod", 
		"4k resolution video", "nature portrait", "photo memory card", "optix lens 24 megapixel"],
	"randomBadQueries": ["vidao","defenetion","heigh", "resalation"],
	"allowAnonymousVisits"	: True,
	"anonymousThreshold" : 1,
	"timeBetweenVisits": 2,
	"timeBetweenActions": 1,
	"defaultPageViewField":"fid28306",
	"randomCustomData": [
		{
			"apiname": "c_context_profile_Retail_Persona",
			"values": ["Celine the Photographer"]
		},
		{
			"apiname": "c_isbot", "values": ["true"]
		}
	],
	"globalFilter":"(@syssource==\"Coveo_web_index - LAUNCHSITECORE-Habitat.dev.local\") (@fz95xlanguage28306==en) (@fz95xlatestversion28306==1) (@falltemplates28306==225F8638261148419B8919A5440A1DA1 NOT @fz95xtemplate28306==(ADB6CA4F03EF4F47B9AC9CE2BA53FF97,FE5DD82648C6436DB87A7C4210C7413B))",
	"scenarios" : [
        {    "name": "HomePageViewAndClick",
    "weight": 3,
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    "events": []}
    ]
}

scenario["events"].append(json.loads(event1))
scenario["events"].append(json.loads(event2))

fileManager.createScenario(scenario_file, scenario)





{
    "keyword1":  {
        "totalCount": 0,
        "results: [ title1, title2]
    }
}

result_list = {}

for q in q_list:
    query = searchApi.search(access_token, organizationId, aq, q, pipeline)

    result = {}

    result['totalCount'] = query['totalCount']
    result['documents'] = []
    i = 0


    for document in query['results']:
        result['documents'].append(document['title'])
        i+=1
        if i >= 10 or  i > len(query['results']):
            break
    
    result_list[q] = result 



with open(result_list_file, 'w') as outfile:
    json.dump(result_list, outfile)
'''


