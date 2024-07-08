import json
json_string = '[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]'
print(json.loads(json_string)[1][2])
