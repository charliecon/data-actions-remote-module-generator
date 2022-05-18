import uuid, json, os

accelerator_object = {
    'id': '',
    'name': '',
    'description': '',
    'origin': 'genesys',
    'type': 'module',
    'classification': 'integration',
    'tags': ['Data Actions', 'Platform API', 'CX as Code', 'Remote Module'],
    'permissions': [
        'integrations:action:view', 
        'bridge:actions:view',
        'integrations:action:add',
        'integrations:action:edit',
        'integrations:action:delete'
    ],
    'products': ['Quality Assurance and Compliance'],
    'documentation': [{}],
    'presentation': [
        {
            'title': 'Page 1',
            'description': 'Please enter the fields below',
            'fields': ['action_name', 'action_category', 'integration_id', 'secure_data_action']
        }
    ]
}

def create_accelerator_file(path_to_data_action, dest_path):
    dest_path = os.path.join(dest_path, 'accelerator.json')
    
    f = open(path_to_data_action)
    data = json.load(f)

    accelerator_object['id'] = str(uuid.uuid4())
    accelerator_object['name'] = data['name'] + ' Data Action Module'
    accelerator_object['description'] = 'This CX as Code remote module performs the following platform API operation: ' + data['name']

    fout = open(dest_path, 'wt')
    fout.write(json.dumps(accelerator_object, indent=4))
    fout.close()

