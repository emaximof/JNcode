x = open('/Users/sgozansky/Downloads/cucumberWithFailed.json', 'r')
 
def remove_fields(json_obj, field_name):
    if isinstance(json_obj, dict):
        # Check if the field_name exists in the dictionary
        if field_name in json_obj:
            del json_obj[field_name]
        
        # Recursively call the function on each value in the dictionary
        for key, value in list(json_obj.items()):
            remove_fields(value, field_name)
            
    elif isinstance(json_obj, list):
        # Recursively call the function on each element in the list
        
        for item in json_obj:
            remove_fields(item, field_name)
        
        
def remove_elemts(obj):
    new_elements = []
    elemnts = obj['elements']
    for element in elemnts:
        if element['type'] == "scenario":
            new_elements.append(element)
    obj['elements'] = new_elements
            
import json
json_obj = json.load(x)
remove_fields(json_obj, 'data')
remove_fields(json_obj, 'steps')
remove_fields(json_obj, 'match')
remove_fields(json_obj, 'output')
#remove_elemts(json_obj)



print(json_obj["name"])
print(json_obj["description"])
print(json_obj["id"])
print(json_obj["uri"])
elemnts = json_obj['elements']
for element in elemnts:
    print(json.dumps(element))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    