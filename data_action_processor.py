import json

def proccess_data_action(path_to_file):
    contract_input = ''
    contract_output = ''
    request_template = ''
    request_url_template = ''
    request_type = ''
    header_values = {}
    success_template = ''
    translation_map_values = {}

    f = open(path_to_file)
    data = json.load(f)
    for attr, val in data.items():
        if attr == 'contract':       
            for k, v in val.items():
                if k == 'input':
                    contract_input = json.dumps(v) 
                if k == 'output':              
                    contract_output = json.dumps(v) 
        elif attr == 'config':
            for k, v in val.items():
                if k == 'request':
                    for rk, rv in v.items(): 
                        if rk == 'requestUrlTemplate':
                            request_url_template = rv
                        if rk == 'requestType':
                            request_type = rv
                        if rk == 'requestTemplate':
                            request_template = rv
                        if rk == 'headers':
                            for hk, hv in rv.items():
                                header_values[hk] = hv
                if k == 'response':
                    for rk, rv in v.items():
                        if rk == 'successTemplate':
                            success_template = rv
                        if rk == 'translationMap':
                            for tk, tv in rv.items():
                                translation_map_values[tk] = tv

    result = {
        "contract_input":     escape_special_chars(str(contract_input)),
        "contract_output":    escape_special_chars(str(contract_output)),
        "requestUrlTemplate": escape_special_chars(request_url_template),
        "requestTemplate":    escape_special_chars(request_template),
        "requestType":        request_type,
        "headers":            header_values,
        "successTemplate":    escape_special_chars(success_template),
        "translationMap":     translation_map_values
    }
    return result

def escape_special_chars(val):
    if val == '':
        return val
    return val.encode('unicode_escape').decode('utf-8').replace('${', '$${').replace('"', '\\"')

def main():
    print('test')

if __name__ == "__main__":
    main()
