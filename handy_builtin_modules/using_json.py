import json

# online docs: https://docs.python.org/3/library/json.html

# convert json object structure to a string
json_string = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print("%s" % json_string)

# convert json string to object structure
json_objs = json.loads(json_string)
print("%s" % repr(json_objs))

