import os, shutil, data_action_processor, resource_file_editor

relative_path_to_data_actions = '../../genesys_src/repos/genesys-cloud-data-actions'
parent_dir_name = 'modules'
consistent_files_dir_name = 'consistent_files'

def create_parent_directory():
    try:
        os.mkdir(parent_dir_name)
    except OSError as error:
        print(error)

def generate_dir(filename):
    dir_name = 'public-api-' + filename.replace('.json', '').lower() + '-data-action-module'
    full_path = os.path.join(parent_dir_name, dir_name)
    path_to_json_file = os.path.join(relative_path_to_data_actions, filename)
    path_to_resource_file = os.path.join(full_path, 'main.tf')

    try:
        os.mkdir(full_path)
    except OSError as error:
        return error

    # Copy consistent files (.gitignore, LICENSE, etc.) into module folder
    consistent_files = os.listdir(consistent_files_dir_name)
    for c in consistent_files:
        shutil.copy(os.path.join(consistent_files_dir_name, c), full_path)
    shutil.copy(path_to_json_file, full_path)

    values = data_action_processor.proccess_data_action(path_to_json_file)
   
    resource_file_editor.insert_values(values, path_to_resource_file)

    return None

def main():
    safety_counter = 0
    limit = 20

    create_parent_directory()

    contents = os.listdir(relative_path_to_data_actions)
    for c in contents:
        safety_counter += 1
        if safety_counter > limit:
            return
        if c.endswith('.json'):            
            error = generate_dir(c)
            if error != None:
                print(error)

def test():
    data_action_processor.proccess_data_action()

if __name__ == '__main__':
    main()