import json
import textwrap

def proccess_data_action(path_to_file):
    f = open(path_to_file)
    data = json.load(f)

    headers = {}
    translation_map = {}
    translation_map_defaults = {}
    for k, v in data['config']['request']['headers'].items():
        headers[k] = v
    for k, v in data['config']['response']['translationMap'].items():
        translation_map[k] = escape_special_chars(v)
    for k, v in data['config']['response']['translationMapDefaults'].items():
        translation_map_defaults[k] = escape_special_chars(v)
    #contract_input = escape_special_chars(json.dumps(data['contract']['input']))
    #contract_output = escape_special_chars(json.dumps(data['contract']['output']))
    request_template = escape_special_chars(data['config']['request']['requestTemplate'])
    request_url_template = escape_special_chars(data['config']['request']['requestUrlTemplate'])
    success_template = escape_special_chars(data['config']['response']['successTemplate'])
    request_type = data['config']['request']['requestType']

    contract_input_decoded = encode_json(data['contract']['input'])
    contract_output_decoded = encode_json(data['contract']['output'])

    result = {
        'name':                   data['name'],
        'contract_input':         contract_input_decoded,
        'contract_output':        contract_output_decoded,
        'requestUrlTemplate':     request_url_template,
        'requestTemplate':        request_template,
        'requestType':            request_type,
        'headers':                headers,
        'successTemplate':        success_template,
        'translationMap':         translation_map,
        'translationMapDefaults': translation_map_defaults
    }

    return result

def escape_special_chars(val):    
    return val.encode('unicode_escape').decode('utf-8').replace('${', '$${').replace('"', '\\"')

def encode_json(data):
    s = json.dumps(data, sort_keys=True, indent=4)
    s = s.replace('": ', '" = ')
    s = reindent(s, 4)
    s = f'jsonencode({s[4:]})'
    return s

def reindent(s, num_spaces):
    s = textwrap.indent(s, ' ' * num_spaces)
    return s

def main():
    f = open('test.json')
    data = json.load(f)
    thing = data['config']['request']['headers']
    print(thing)
    
if __name__ == "__main__":
    main()
