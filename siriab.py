"""
Enhanced testing support is available in this script.

Prerequisite:
    - The 'pytest' package must be installed.
    - To install: run `pip install pytest`

How to run tests (if pytest is installed):
    1. To run all tests:
       `pytest siriab.py`
    2. To run a specific test case:
       `pytest siriab.py::test_solve_arrow_rotation`

    Available test functions:
        - test_solve_arrow_rotation
        - test_solve_asphalt_patching
        - test_solve_rain_water_tank

If you don't wish to use the enhanced testing option,
you can still run the script as a regular Python file:
    `python siriab.py`
check in the `run_manually` section to run solutions manually as of your choice

"""
# ----------------- Solutions -------------------


def solve_arrow_rotation(s: str):
    dir_counts = {}
    # ^ - w counts
    # v - x counts
    # < - y counts
    # > - z counts
    # aggregate direction-based count of arrows
    for letter in s:
        dir_counts[letter] = dir_counts.get(letter, 0) + 1

    # Let's get the highest value of arrows present in the same direction
    max_same_dir_counts = max(dir_counts.values())

    # remaining arrows are in different direction, so need to rotate them
    # their count would be total_arrows - max_same_dir_counts
    # And this would be our result
    return len(s) - max_same_dir_counts


def solve_rain_water_tank(s: str):
    # The approach would be like will start iterating from left to right
    # will check for available of space in left and right when a Home is found,
    # will check if a tank is present in left or right, if not will add a tank
    # If tank is available in either side already, will skip and move ahead

    # For that reason to track where are we placing a tank,
    # made list so that it would be easy to update and checking in surrondings
    home = 'H'
    tank = 'T'
    empty = '-'

    row_house = list(s)
    n = len(s)
    tank_added = 0

    # start iterations
    for i, place in enumerate(row_house):
        # If a home is found then only will check for its surrounding
        if place is home:
            # check if a tank is available in its left
            tank_in_left = i > 0 and row_house[i-1] is tank

            # check if a tank is available in its right
            tank_in_right = i + 1 < n and row_house[i+1] is tank

            if tank_in_left or tank_in_right:
                continue

            # trying placing on right-side first
            if i + 1 < n and row_house[i+1] is empty:
                row_house[i+1] = tank
                tank_added += 1
            elif i > 0 and row_house[i-1] is empty:
                row_house[i-1] = tank
                tank_added += 1
            # No empty space available
            else:
                return -1

    return tank_added


def solve_asphalt_patching(road: str):
    n = len(road)
    patch_added = 0
    current_loc = 0

    pothole = 'X'

    # iteration from 0th location until last, if a pothole found,
    # will add a patch, and skip next three consecutive segments
    while current_loc < n:
        # if pothole found
        if road[current_loc] is pothole:
            patch_added += 1

            # move the pointer to after three segments
            current_loc += 3

        else:
            # move current location to next segment
            current_loc += 1

    return patch_added


# ---------- Tests (Pytest style) ----------

try:
    import pytest

    @pytest.mark.parametrize("arrows, expected", [
        ("^vv<v", 2),
        ("v>>>vv", 3),
        (">>><<<", 3),
        ("<<<", 0),
    ])
    def test_solve_arrow_rotation(arrows, expected):
        assert solve_arrow_rotation(arrows) == expected

    @pytest.mark.parametrize("house, expected", [
        ("-H-HH--", 2),
        ("H", -1),
        ("-H-H-H-H-H", 3),
    ])
    def test_solve_rain_water_tank(house, expected):
        assert solve_rain_water_tank(house) == expected

    @pytest.mark.parametrize("road, expected", [
        (".X..X", 2),
        ("X.XXXXX.X.", 3),
        ("XX.XXX..", 2),
        ("XXXX", 2)
    ])
    def test_solve_asphalt_patching(road, expected):
        assert solve_asphalt_patching(road) == expected
except ImportError:
    print("⚠️  Pytest is not installed. Please run: pip install pytest")
    # exit(1)  # commented to allow the file to execute even without pytest pkg


def run_manually():
    # below lines added for manual testing each solution separately
    # I've just added an example
    print("🔍 Running solutions manually!")
    road, expected = ".X..X", 2
    print(solve_asphalt_patching(road) == expected)

    house, expected = "-H-H-H-H-H", 3
    print(solve_rain_water_tank(house) == expected)

    arrows, expected = "v>>>vv", 3
    print(solve_arrow_rotation(arrows) == expected)


# ---------- Optional: Run manually ----------
if __name__ == '__main__':
    try:
        import pytest
        # to trigger the pytests cases automatically
        pytest.main([__file__])  # If want to disable, comment it out
        print("✅ Pytest available, All test cases were executed successfully.")

        # if you want to run solutions manually, you can enable below
        # run_manually()
    except ImportError:
        print("⚠️  Pytest is not installed. You can run solutions manually.")
        # exit(1)

        # allowing solutions to run manully if pytest is not available
        run_manually()
