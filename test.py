from type_analyzer import get_not_covered_types, get_types_from_file
from utils import load_json
from typing import Dict


def test():
    types_file = 'types-after-gen6.json'
    types: Dict[str, any] = load_json(types_file)
    my_team_file = 'my-types.txt'
    my_team = get_types_from_file(my_team_file)
    print(get_not_covered_types(types, my_team))

test()