import searchApi

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