contract_input_placeholder_id           = 'contract_input_placeholder'
contract_output_placeholder_id          = 'contract_output_placeholder'
request_url_template_placeholder_id     = 'request_url_template_placeholder'
request_type_placeholder_id             = 'request_type_placeholder'
request_template_placeholder_id         = 'request_template_placeholder'
headers_placeholder_id                  = 'headers_placeholder'
success_template_placeholder_id         = 'success_template_placeholder'
translation_map_placeholder_id          = 'translation_map_placeholder'
translation_map_defaults_placeholder_id = 'translation_map_defaults_placeholder'

path_to_template_main = 'template_files/template_main.tf'

def insert_values(values, path):
    fin = open(path_to_template_main, 'rt')
    fout = open(path, 'wt')

    for line in fin:
        line_to_write = get_line(values, line)
        if contains_nested_object(line_to_write):
            lines_to_write = get_nested_object_lines(line, line_to_write, values)
            for l in lines_to_write:
                fout.write(l)
        else:
            fout.write(line_to_write)
    
    fin.close()
    fout.close()

##
# Search line for placeholder. 
# If found - swap it out for the real value stored in 'values' object
##
def get_line(values, line):
    # the place holder id : the value to replace it with
    pairs = {
        contract_input_placeholder_id:           values['contract_input'],
        contract_output_placeholder_id:          values['contract_output'],
        request_url_template_placeholder_id:     values['requestUrlTemplate'],
        request_type_placeholder_id:             values['requestType'],
        request_template_placeholder_id:         values['requestTemplate'],
        headers_placeholder_id:                  values['headers'],
        success_template_placeholder_id:         values['successTemplate'],
        translation_map_placeholder_id:          values['translationMap'],
        translation_map_defaults_placeholder_id: values['translationMapDefaults']
    }

    for k, v in pairs.items():
        if k in line:
            if k == headers_placeholder_id:
                return headers_placeholder_id
            if k == translation_map_placeholder_id:
                return translation_map_placeholder_id
            if k == translation_map_defaults_placeholder_id:
                return translation_map_defaults_placeholder_id
            return line.replace(k, v)
    return line

def get_nested_object_lines(line, line_to_write, values):
    placeholder_id, items, opener = determine_attribute_values(line_to_write, values) 
    all_lines_to_return = []

    if len(items.items()) > 0:
        all_lines_to_return.append(line.replace(placeholder_id, opener))
        all_lines = get_nested_attr_lines(items)
        for l in all_lines:
            all_lines_to_return.append(l)
    else:
        all_lines_to_return.append(line.replace(placeholder_id, ''))
    
    return all_lines_to_return

def get_nested_attr_lines(pairs):
    all_lines = []    
    for k, v in pairs.items():
        val = v
        if type(v) == str:                
            val = f'"{v}"'                
        all_lines.append(f'\t\t\t{k} = {val}\n')
    all_lines.append('\t\t}\n')
    return all_lines

def contains_nested_object(line):
    if headers_placeholder_id in line:
        return True
    if translation_map_placeholder_id in line:
        return True
    if translation_map_defaults_placeholder_id in line:
        return True 
    return False

def determine_attribute_values(line, values):
    if headers_placeholder_id in line:
        return headers_placeholder_id, values['headers'], 'headers = {'
    elif translation_map_defaults_placeholder_id in line:
        return translation_map_defaults_placeholder_id, values['translationMapDefaults'], 'translation_map_defaults = {'
    else:
        return translation_map_placeholder_id, values['translationMap'], 'translation_map = {'

if __name__ == '__main__':
    print('Execute runner.sh')