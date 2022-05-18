import os, shutil, data_action_processor, resource_file_writer, readme_writer, accelerator, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--local', action='store_true')

default_path_to_data_actions = 'path/to/data-actions'
parent_dir_name              = 'modules'
consistent_files_dir_name    = 'consistent_files'
local_provider_path          = './test_tf_files/local_provider.tf'
use_local_provider           = False

##
# Copy consistent files (.gitignore, LICENSE, etc.) into remote module folder
##
def move_consistent_files_to_module_folder(json_file_path, path_to_module):
    consistent_files = os.listdir(consistent_files_dir_name)
    for c in consistent_files:
        # If running for testing purposes - use sideload as provider to speed up tests.
        if c == 'provider.tf' and use_local_provider:
            shutil.copy(local_provider_path, path_to_module)        
        else:
            shutil.copy(os.path.join(consistent_files_dir_name, c), path_to_module)
    # Copy the original data action json file into the repo
    shutil.copy(json_file_path, path_to_module)

def generate_dir(path):
    filename = os.path.basename(path).replace('.json', '')
    dir_name = f'public-api-{filename.lower()}-data-action-module'
    full_path = os.path.join(parent_dir_name, dir_name)
    
    path_to_resource_file = os.path.join(full_path, 'main.tf')
    path_to_readme_file = os.path.join(full_path, 'README.md')

    try:
        os.mkdir(full_path)
    except OSError as error:
        print(error)
        return

    move_consistent_files_to_module_folder(path, full_path)

    values = data_action_processor.proccess_data_action(path)
   
    resource_file_writer.insert_values(values, path_to_resource_file)  
    readme_writer.insert_values(dir_name, values['name'], path_to_readme_file)

    accelerator.create_accelerator_file(path, full_path)

def generate_module_from_file(file_path):
    generate_dir(file_path)

def generate_modules_from_dir(dir_path):
    contents = os.listdir(dir_path)
    for c in contents:
        if c.endswith('.json'):            
            generate_module_from_file(os.path.join(dir_path, c))

def create_parent_directory():
    try:
        os.mkdir(parent_dir_name)
    except OSError as error:
        print(error)

def main(args):
    create_parent_directory()
    path = default_path_to_data_actions
    if len(args) > 2 and use_local_provider:
        path = args[2]
    elif len(args) > 1 and use_local_provider is False:
        path = args[1]
    
    if os.path.isfile(path) and str(path).endswith('.json'):
        generate_module_from_file(path)
    elif os.path.isdir(path):
        generate_modules_from_dir(path)   
    else:
        print('The provided path is invalid or cannot be found.')

if __name__ == '__main__':
    args, left = parser.parse_known_args()
    use_local_provider = args.local
    main(sys.argv)