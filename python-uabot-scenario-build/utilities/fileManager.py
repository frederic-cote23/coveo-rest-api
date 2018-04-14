import json

def readDict (q_word_file):
    with open(q_word_file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def createScenario(scenario_file, scenario):
    with open(scenario_file, 'w') as f:
        f.write(json.dumps(scenario))

def readConfig(config_file):
    return json.load(open(config_file))