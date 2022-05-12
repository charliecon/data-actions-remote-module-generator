## Data Action Remote Module Generator

A tool to generate Terraform remote modules for Genesys Cloud data actions.

### Installation 

```
git clone https://github.com/charliecon/data-actions-remote-module-generator.git
```

### How To

To generate the module(s), execute the script inside `runner.sh`, passing the path to the data action JSON file, or the path to a parent directory containing these files. 

```
./runner.sh <path>
```

The output is sent to a directory called `modules`.

You can also set the variable `default_path_to_data_actions` inside `main.py` to the relative path to the data action(s) and omit the command line argument. 

### Testing

To run tests on the directories created inside `/modules`:

```
./tests.sh <path>
```

This script will initialize Terraform within all of the repos created to check for syntax errors. If you wish to test mulitple modules, you can speed up the process greatly by using a locally compiled version of the provider and running the following command:

```
./tests.sh <path> --local
```

Steps on how to build the provider can be found [here](https://github.com/MyPureCloud/terraform-provider-genesyscloud "Opens the terraform-provider-genesyscloud repository of GitHub")

**Note:** The module repo name is generated based on the JSON file name. For example, the file `Get-User-ID-By-Email.json` will create the module `public-api-get-user-id-by-email-data-action-module`

*Python Version Used: 3.9.5*

