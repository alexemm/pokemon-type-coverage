from typing import Dict, Set
from utils import read_file


def get_advantageous_types(types: Dict[str, any], pkmn_type: str) -> Set[str]:
    return set(types[pkmn_type]["strengths"])


def get_types_from_file(file: str) -> Set[str]:
    f = read_file(file)
    return set([type for types in f for type in types.split(" ")])


def get_strengths_of_team(types: Dict[str, any], pkmn_team: Set[str]) -> Set[str]:
    strengths: Set[str] = set()
    for type in pkmn_team:
        strengths |= get_advantageous_types(types, type)
    return strengths


def get_all_pkmn_types(types: Dict[str, any]) -> Set[str]:
    return set(types.keys())


def get_not_covered_types(types: Dict[str, any], pkmn_team: Set[str]) -> Set[str]:
    return get_all_pkmn_types(types) - get_strengths_of_team(types, pkmn_team)
