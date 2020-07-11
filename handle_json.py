import json

f = open('gsmarena.json')
data = json.load(f)
f.close()

list_key = ['brand', 'name', 'models', 'color', 'ram', 'storage', 'rom', 'screen', 'screen_size', 'sim', 'os',
            'behind_camera', 'front_camera', 'url', 'error_url']


def testthoi():
    pass


new_dict = {}
for ele in list_key:
    new_dict[ele] = '-1'
for items in data:
    for ele in list_key:
        for key in items.keys():
            if ele == key:
                new_dict[ele] = items[key]
    with open("new_gsmarena.json", "a+") as write_file:
        json.dump(new_dict, write_file)
        write_file.write(',')
