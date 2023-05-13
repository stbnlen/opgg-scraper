import pytest
from utils.create_object_dict import create_objects_dict

def test_create_objects_dict():
    result = create_objects_dict(
        result_texts="Victory",
        champion="Ashe",
        kill=10,
        death=2,
        assist=8,
        damage_dealt=15000,
        damage_taken=10000,
        game_type="Ranked",
        length=30,
        percentage=70,
        tier="Gold",
        cs=200,
        cs_per_minute=6,
        game_items=["Infinity Edge", "Runaan's Hurricane"],
        wards=5,
        baron=True,
        dragon=False,
        tower=True,
    )

    expected_result = {
        "result": "Victory",
        "champion": "Ashe",
        "kill": 10,
        "death": 2,
        "assist": 8,
        "dmg_dealt": 15000,
        "dmg_taken": 10000,
        "game_type": "Ranked",
        "length": 30,
        "kill_percentage": 70,
        "average_tier": "Gold",
        "cs": 200,
        "cs_per_minute": 6,
        "items": ["Infinity Edge", "Runaan's Hurricane"],
        "control_wards": 5,
        "baron": True,
        "dragon": False,
        "tower": True,
    }

    assert result == expected_result

def test_create_objects_dict_missing_argument():
    with pytest.raises(TypeError):
        create_objects_dict(
            result_texts="Victory",
            champion="Ashe",
            kill=10,
            death=2,
            assist=8,
            damage_dealt=15000,
            damage_taken=10000,
            game_type="Ranked",
            length=30,
            percentage=70,
            tier="Gold",
            cs=200,
            cs_per_minute=6,
            game_items=["Infinity Edge", "Runaan's Hurricane"],
            wards=5,
            baron=True,
            dragon=False,
            # Missing 'tower' argument
        )

def test_create_objects_dict_extra_argument():
    with pytest.raises(TypeError):
        create_objects_dict(
            result_texts="Victory",
            champion="Ashe",
            kill=10,
            death=2,
            assist=8,
            damage_dealt=15000,
            damage_taken=10000,
            game_type="Ranked",
            length=30,
            percentage=70,
            tier="Gold",
            cs=200,
            cs_per_minute=6,
            game_items=["Infinity Edge", "Runaan's Hurricane"],
            wards=5,
            baron=True,
            dragon=False,
            tower=True,
            extra_arg=123  # Extra argument not expected by the function
        )
