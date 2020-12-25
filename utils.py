from typing import Optional, List

import json


def load_json(file) -> Optional[any]:
    json_obj = None
    with open(file) as f:
        json_obj = json.load(f)
    return json_obj


def write_json(json_obj, file):
    with open(file, 'w') as f:
        json.dump(json_obj, f)


def create_json_of_types():
    """
    The source of the types (little pre-processing step):
    https://github.com/filipekiss/pokemon-type-chart/blob/master/types.json
    :return:
    """
    file: str = "types.json"
    json_obj = load_json(file)
    new_json_obj = {}
    for type_obj in json_obj:
        new_json_obj[type_obj['name']] = {}
        for attribute in ["immunes", "weaknesses", "strengths"]:
            new_json_obj[type_obj['name']][attribute] = type_obj[attribute]
    write_json(new_json_obj, "types-after-gen6.json")


def read_file(file: str) -> List[str]:
    text: List[str] = []
    with open(file) as f:
        text = f.read().splitlines()
    return text
