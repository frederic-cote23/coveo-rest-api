import searchApi
import json
import fileManager

access_token = 'xxcb8b6a78-16a2-4aec-b9a6-27df2ea0f5bc'
organizationId = 'coveolearningbasicanalytics'
aq = '@source="App Store"'
pipeline = 'default'

q = 'apple'
q_word_file = 'dic.text'
q_list = fileManager.readDict(q_word_file)

result_list_file = 'result_list.json'

'''
{
    "keyword1":  {
        "totalCount": 0,
        "results: [ title1, title2]
    }
}
'''
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



