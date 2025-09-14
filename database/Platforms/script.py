import json

def compare_json(a_file, b_file, output_file):
    with open(a_file, 'r') as a:
        data_a = json.load(a)
    with open(b_file, 'r') as b:
        data_b = json.load(b)
    
    missing_keys = {key: data_a[key] for key in data_a if key not in data_b}

    with open(output_file, 'w') as output:
        json.dump(missing_keys, output, indent=4)

sku1 = input("Enter platform name for main sku")
sku2 = input("Enter platform name for secondary sku")
output_file = 'missing_keys.json'

compare_json(sku1 + '/sku-packages.json', sku2 + '/sku-packages.json, output_file)
