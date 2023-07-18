import json

my_data = {"a": [1, 2, 3, 4],
           "b": {1: 1, 2: 2},
           3: "Hello",
           4: True,
           5: ("a", "b")}

byte_str = json.dumps(my_data)

unpacked = json.loads(byte_str)

print(unpacked["4"])