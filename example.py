import re

def read_config(file_path):
    with open(file_path, 'r') as file:
        config_data = file.read()
    return config_data

def extract_variable_value(config_data, variable_name):
    # Assuming the variable assignment follows the pattern 'variable_name="value"'
    pattern = f'{variable_name}="([^"]*)"'
    match = re.search(pattern, config_data)
    if match:
        return match.group(1)
    else:
        return None

# Path to your .config file
config_file_path = '.apiKey'

# Read the content of the .config file
config_data = read_config(config_file_path)

# Extract the value of my_var
my_var = extract_variable_value(config_data, 'openai_key')

# Use the value in your code
print(my_var)