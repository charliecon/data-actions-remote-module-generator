import os, shutil, data_action_processor, resource_file_writer, readme_writer, sys

relative_path_to_data_actions = '../../genesys_src/repos/genesys-cloud-data-actions'
parent_dir_name               = 'modules'
consistent_files_dir_name     = 'consistent_files'
local_provider_path           = './test_tf_files/local_provider.tf'
is_for_tests                  = False

def create_parent_directory():
    try:
        os.mkdir(parent_dir_name)
    except OSError as error:
        print(error)

def generate_dir(filename):
    data_action_name = filename.replace('.json', '').replace('-', ' ')
    dir_name = 'public-api-' + filename.replace('.json', '').lower() + '-data-action-module'
    full_path = os.path.join(parent_dir_name, dir_name)
    path_to_json_file = os.path.join(relative_path_to_data_actions, filename)
    path_to_resource_file = os.path.join(full_path, 'main.tf')
    path_to_readme_file = os.path.join(full_path, 'README.md')

    try:
        os.mkdir(full_path)
    except OSError as error:
        print(error)
        return

    # Copy consistent files (.gitignore, LICENSE, etc.) into module folder
    consistent_files = os.listdir(consistent_files_dir_name)
    for c in consistent_files:
        # If running for testing purposes - use sideload as provider to speed up tests.
        if c == 'provider.tf' and is_for_tests:
            shutil.copy(local_provider_path, full_path)
        else:
            shutil.copy(os.path.join(consistent_files_dir_name, c), full_path)
    shutil.copy(path_to_json_file, full_path)

    values = data_action_processor.proccess_data_action(path_to_json_file)
   
    resource_file_writer.insert_values(values, path_to_resource_file)   
    readme_writer.insert_values(dir_name, data_action_name, path_to_readme_file)

    return None

def main():
    counter = 0
    limit = 3

    create_parent_directory()

    contents = os.listdir(relative_path_to_data_actions)
    for c in contents:
        counter += 1
        if counter > limit:
            return
        if c.endswith('.json'):            
            generate_dir(c)

if __name__ == '__main__':
    is_for_tests = len(sys.argv) > 1
    main()