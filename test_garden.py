import ast
from pathlib import Path

from garden import (
    RIPE_DAYS_FROM_SEED,
    WATER_MAX,
    advance_day,
    create_garden,
    dig,
    get_cell,
    harvest,
    is_in_bounds,
    plant,
    water,
)
from cli_view import GardenPrinter


# def setup_seeded_cell(rows=3, cols=3, row=1, col=1, crop="carrot"):
#     garden = create_garden(rows, cols)
#     assert dig(garden, row, col) is True
#     assert plant(garden, row, col, crop) is True
#     return garden


# def test_create_garden_builds_empty_grid():
#     garden = create_garden(2, 3)

#     assert len(garden) == 2
#     assert len(garden[0]) == 3
#     assert get_cell(garden, 0, 0) == {"state": "empty", "crop": None, "water": 0, "days_as_seed": 0}


# def test_bounds_and_get_cell_out_of_bounds():
#     garden = create_garden(2, 2)

#     assert is_in_bounds(garden, 0, 0) is True
#     assert is_in_bounds(garden, -1, 0) is False
#     assert is_in_bounds(garden, 2, 0) is False
#     assert get_cell(garden, 5, 5) is None


# def test_dig_only_allowed_on_empty():
#     garden = create_garden(2, 2)

#     assert dig(garden, 0, 0) is True
#     assert get_cell(garden, 0, 0)["state"] == "hole"
#     assert dig(garden, 0, 0) is False


# def test_plant_only_allowed_on_hole():
#     garden = create_garden(2, 2)

#     assert plant(garden, 0, 0, "carrot") is False
#     assert dig(garden, 0, 0) is True
#     assert plant(garden, 0, 0, "carrot") is True

#     cell = get_cell(garden, 0, 0)
#     assert cell["state"] == "seed"
#     assert cell["crop"] == "carrot"
#     assert cell["water"] == 0
#     assert cell["days_as_seed"] == 0


# def test_water_only_allowed_for_seed():
#     garden = create_garden(2, 2)

#     assert water(garden, 0, 0) is False
#     assert dig(garden, 0, 0) is True
#     assert water(garden, 0, 0) is False

#     assert plant(garden, 0, 0, "tomato") is True
#     assert water(garden, 0, 0) is True


# def test_water_has_maximum_value():
#     garden = setup_seeded_cell()

#     for _ in range(WATER_MAX + 5):
#         assert water(garden, 1, 1) is True

#     assert get_cell(garden, 1, 1)["water"] == WATER_MAX


# def test_advance_day_reduces_water_not_below_zero():
#     garden = setup_seeded_cell()

#     advance_day(garden)
#     assert get_cell(garden, 1, 1)["water"] == -1

#     advance_day(garden)
#     assert get_cell(garden, 1, 1)["water"] == -2


# def test_growth_to_ripe_takes_three_qualifying_days():
#     garden = setup_seeded_cell(crop="lettuce")

#     for expected_days in range(1, RIPE_DAYS_FROM_SEED):
#         # WATER_MAX is 1, so we preload enough water for a qualifying day.
#         get_cell(garden, 1, 1)["water"] = 2
#         advance_day(garden)
#         cell = get_cell(garden, 1, 1)
#         assert cell["state"] == "seed"
#         assert cell["days_as_seed"] == expected_days

#     get_cell(garden, 1, 1)["water"] = 2
#     advance_day(garden)
#     assert get_cell(garden, 1, 1)["state"] == "ripe"


# def test_harvest_only_allowed_on_ripe_and_resets_cell():
#     garden = setup_seeded_cell(crop="pumpkin")

#     assert harvest(garden, 1, 1) is None

#     for _ in range(RIPE_DAYS_FROM_SEED):
#         get_cell(garden, 1, 1)["water"] = 2
#         advance_day(garden)

#     assert get_cell(garden, 1, 1)["state"] == "ripe"

#     result = harvest(garden, 1, 1)
#     assert result == "pumpkin"
#     assert get_cell(garden, 1, 1) == {"state": "empty", "crop": None, "water": 0, "days_as_seed": 0}


# def test_mutating_functions_handle_out_of_bounds_cleanly():
#     garden = create_garden(2, 2)

#     assert dig(garden, 10, 10) is False
#     assert plant(garden, 10, 10, "carrot") is False
#     assert water(garden, 10, 10) is False
#     assert harvest(garden, 10, 10) is None


# def test_core_logic_has_no_cli_dependency():
#     garden = create_garden(1, 1)

#     assert dig(garden, 0, 0) is True
#     assert plant(garden, 0, 0, "bean") is True
#     assert water(garden, 0, 0) is True
#     assert advance_day(garden) is True


# def test_printer_renders_ascii_grid_with_borders():
#     garden = create_garden(2, 2)
#     assert dig(garden, 0, 0) is True
#     assert plant(garden, 0, 0, "carrot") is True

#     output = GardenPrinter().render(garden)

#     assert "  +---+---+" in output
#     assert "0| . |   |" in output
#     assert "1|   |   |" in output
#     assert "  0   1" in output


def test_aufgabe_1_tomato_file_exists():
    assert Path("harvests/tomato.txt").exists()

def test_aufgabe_2_quit_command_exists():
    source = Path("main.py").read_text(encoding="utf-8")
    tree = ast.parse(source)

    print_help_table_node = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "print_help_table":
            print_help_table_node = node
            break

    assert print_help_table_node is not None

    rows_list = None
    for node in print_help_table_node.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "rows"
            and isinstance(node.value, ast.List)
        ):
            rows_list = node.value
            break

    assert rows_list is not None

    row_values = set()
    for element in rows_list.elts:
        if isinstance(element, ast.Tuple) and len(element.elts) == 3:
            if all(isinstance(item, ast.Constant) and isinstance(item.value, str) for item in element.elts):
                row_values.add(tuple(item.value.lower() for item in element.elts))

    assert ("quit", "exit the simulator", "quit") in row_values


def test_aufgabe_3_harvest_tomato_prints_message(capsys):
    garden = create_garden(1, 1)
    assert dig(garden, 0, 0) is True
    assert plant(garden, 0, 0, "tomato") is True

    cell = get_cell(garden, 0, 0)
    cell["state"] = "ripe"

    assert harvest(garden, 0, 0) == "tomato"

    captured = capsys.readouterr()
    assert "created file 'tomato.txt'" in captured.out.lower()
