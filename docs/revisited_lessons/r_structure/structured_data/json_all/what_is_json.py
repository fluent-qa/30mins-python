#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from typing import Dict, Any

__all__ = [
    "json_to_dict",
    "read_json_file"
]

import rich

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


def json_to_dict() -> Dict:
    rich.print(type(json_str))
    rich.print_json(json_str)
    dict_demo = json.loads(json_str)
    return dict_demo

def get_json_value(key:str)->Any:
    return json_to_dict()[key]

def read_json_file(file_name: str='country.json')->Dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

print(json.loads(json_str)["name"])
print(get_json_value("name"))

json_array_str="[1,2,3,435]"

print(json.loads(json_array_str)[0])