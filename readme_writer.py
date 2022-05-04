path_to_template_readme      = 'template_files/template_README.md'
module_repo_name_placeholder = 'module_repo_name'
data_action_name_placeholder = 'data_action_name'

def insert_values(repo_name, data_action_name, path):
    fin = open(path_to_template_readme, 'rt')
    fout = open(path, 'wt')

    for line in fin:
        if module_repo_name_placeholder in line:
            fout.write(line.replace(module_repo_name_placeholder, repo_name))
        elif data_action_name_placeholder in line:
            fout.write(line.replace(data_action_name_placeholder, data_action_name))
        else:
            fout.write(line)
    
    fin.close()
    fout.close()