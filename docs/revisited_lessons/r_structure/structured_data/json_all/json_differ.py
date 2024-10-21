#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from pprint import pprint

from deepdiff import DeepDiff

t1 = {1: 1, 2: 2, 3: 3}
t2 = {1: 1, 2: "2", 3: 3}

different_result = DeepDiff(t1, t2, verbose_level=0)

for key, item in different_result.items():
    print("change_type", key)
    print("change_details:")
    for element in item.values():
        print(element)

pprint(DeepDiff(t1, t2, verbose_level=0), indent=2)

json_str = """
{
   "name": "China",
   "population": 1431002651,
   "capital": "Beijing",
   "languages": [
      "Chinese"
   ]
}

"""

json_str_2 = """
{
    "name": "China",
    "population": "TEST",
    "capital": "Beijing",
    "languages": [
        "Chinese"
    ],"students": {
        "name": "name",
        "age":18
    }
}
"""

d1 = json.loads(json_str)
d2 = json.loads(json_str_2)
new_result = DeepDiff(d1, d2, verbose_level=2)
print(new_result.to_json())

for key, item in new_result.items():
    print("change_type:", key)
    print("change_details:")
    for element in item.values():
        for key,value in item.items():
            print(f'{key}:{value}')
