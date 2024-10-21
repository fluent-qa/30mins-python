"""
json is a string after all.

1. json to dict
2. json to dataclass
3. dict to json
4. dict to dataclass
5. dataclass to json
6. pydantic to json
7. json to pydantic class/any entity
8. find key in dict or json
"""
import json
from typing import Dict, Union, Any

import jmespath
from deepdiff import DeepDiff
from dotty_dict import dotty
from pydantic import BaseModel


def json_to_dict(json_str: str, **kwargs) -> Dict:
    return json.loads(json_str, **kwargs)


def json_file_to_dict(file_name: str, **kwargs) -> Dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f, **kwargs)
    return data


def object_to_json(obj: Union[BaseModel, Any], **kwargs) -> str:
    return obj.json(**kwargs)


def find_value_by_keypath(key_path: str, json_str: str) -> Any:
    return jmespath.search(expression=key_path, data=json_str)


def set_value_by_keypath(json_dict_eq: Dict | str, key_path: str, to_value: Any) -> Dict:
    dot = dotty(json_dict_eq)
    dot[key_path] = to_value
    return dot.to_dict()


def differ_json(origin_json: Union[str, dict, Any],
                changed_json: Union[str, dict, Any]) -> Dict:
    return DeepDiff(origin_json, changed_json, verbose_level=0).to_dict()
