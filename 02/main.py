def get_puzzle_input(file_path):
    try:
        with open(file_path, "r") as file:
            puzzle_input = file.readlines()

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print("An error occurred:", e)

    return puzzle_input


def process_input(puzzle_input):
    games_dict = {}

    for line in puzzle_input:
        game_id, cube_pulls = line.split(":")
        game_id = game_id.strip()
        cube_pulls = cube_pulls.strip().split(";")
        cube_pulls = [cube_pull.strip().split(",") for cube_pull in cube_pulls]
        games_dict[game_id] = cube_pulls

    return games_dict


def part_1(puzzle_input):
    MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

    games_dict = process_input(puzzle_input)
    valid_games = []

    for game, cube_pulls in games_dict.items():
        is_valid_game = True
        for cube_pull in cube_pulls:
            for cube in cube_pull:
                number, color = cube.strip().split()
                if MAX_CUBES[color] < int(number):
                    is_valid_game = False
                    break
            if is_valid_game is False:
                break
        if is_valid_game is True:
            valid_games.append(game)

    game_number_sum = 0

    for game in valid_games:
        game_number = int(game[4:])
        game_number_sum += game_number

    return game_number_sum


def part_2(puzzle_input):
    games_dict = process_input(puzzle_input)
    min_cubes_per_game = {}

    for game, cube_pulls in games_dict.items():
        min_cubes_color = {}
        for cube_pull in cube_pulls:
            for cube in cube_pull:
                number, color = cube.strip().split()
                if color in min_cubes_color:
                    if min_cubes_color[color] < int(number):
                        min_cubes_color[color] = int(number)
                else:
                    min_cubes_color[color] = int(number)
        min_cubes_per_game[game] = min_cubes_color

    powers = []

    for min_cubes in min_cubes_per_game.values():
        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        powers.append(power)

    sum_of_powers = sum(powers)

    return sum_of_powers


def __main__():
    puzzle_input = get_puzzle_input("02/input.txt")

    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    __main__()
