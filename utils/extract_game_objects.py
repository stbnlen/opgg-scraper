from classes.GameStats import GameStatsExtractor
from classes.ListLengthError import ListLengthError
from utils.create_object_dict import create_objects_dict
from typing import Dict


def extract_game_objects(
    game_stats: GameStatsExtractor, summoner_name: str
) -> Dict[str, any]:
    (
        result_texts,
        game_type,
        kill,
        death,
        assist,
        length,
        champion,
        percentage,
        tier,
        cs,
        cs_per_minute,
        wards,
    ) = game_stats.extract_game_results()
    damage_dealt = game_stats.get_damage(summoner_name, "dealt")
    damage_taken = game_stats.get_damage(summoner_name, "taken")
    game_items = game_stats.get_game_items()
    baron, dragon, tower = game_stats.get_game_objectives()

    if not all(
        len(lst) == len(result_texts)
        for lst in [
            champion,
            kill,
            death,
            assist,
            damage_dealt,
            damage_taken,
            game_type,
            length,
            percentage,
            tier,
            cs,
            cs_per_minute,
            game_items,
            wards,
            baron,
            dragon,
            tower,
            result_texts,
        ]
    ):
        raise ListLengthError("Las listas tienen longitudes diferentes")

    return create_objects_dict(
        result_texts,
        champion,
        kill,
        death,
        assist,
        damage_dealt,
        damage_taken,
        game_type,
        length,
        percentage,
        tier,
        cs,
        cs_per_minute,
        game_items,
        wards,
        baron,
        dragon,
        tower,
    )
