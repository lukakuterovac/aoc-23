def get_puzzle_input(file_path):
    try:
        with open(file_path, "r") as file:
            puzzle_input = file.readlines()

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print("An error occurred:", e)

    return puzzle_input


def part_1(puzzle_input):
    numbers = "0123456789"
    number = ""
    is_adjacent_to_symbol = False
    part_numbers = []

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if puzzle_input[i][j] in numbers:
                number += puzzle_input[i][j]
                # Top left
                try:
                    if puzzle_input[i - 1][j - 1] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Top
                try:
                    if puzzle_input[i - 1][j] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Top right
                try:
                    if puzzle_input[i - 1][j + 1] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Left
                try:
                    if puzzle_input[i][j - 1] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Right
                try:
                    if puzzle_input[i][j + 1] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Bottom left
                try:
                    if puzzle_input[i + 1][j - 1] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Bottom
                try:
                    if puzzle_input[i + 1][j] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
                # Bottom right
                try:
                    if puzzle_input[i + 1][j + 1] not in numbers + "." + "\n":
                        is_adjacent_to_symbol = True
                except IndexError:
                    pass
            else:
                if is_adjacent_to_symbol is True:
                    part_numbers.append(int(number))
                is_adjacent_to_symbol = False
                number = ""

    return sum(part_numbers)


def part_2(puzzle_input):
    numbers = "0123456789"
    number = ""
    is_adjacent_to_symbol = False
    index_gears = {}
    gear_ratios = []

    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if puzzle_input[i][j] in numbers:
                number += puzzle_input[i][j]
                # Top left
                try:
                    if puzzle_input[i - 1][j - 1] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i - 1},{j - 1}"
                except IndexError:
                    pass
                # Top
                try:
                    if puzzle_input[i - 1][j] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i - 1},{j}"
                except IndexError:
                    pass
                # Top right
                try:
                    if puzzle_input[i - 1][j + 1] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i - 1},{j + 1}"
                except IndexError:
                    pass
                # Left
                try:
                    if puzzle_input[i][j - 1] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i},{j - 1}"
                except IndexError:
                    pass
                # Right
                try:
                    if puzzle_input[i][j + 1] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i},{j + 1}"
                except IndexError:
                    pass
                # Bottom left
                try:
                    if puzzle_input[i + 1][j - 1] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i + 1},{j - 1}"
                except IndexError:
                    pass
                # Bottom
                try:
                    if puzzle_input[i + 1][j] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i + 1},{j}"
                except IndexError:
                    pass
                # Bottom right
                try:
                    if puzzle_input[i + 1][j + 1] == "*":
                        is_adjacent_to_symbol = True
                        index = f"{i + 1},{j + 1}"
                except IndexError:
                    pass
            else:
                if is_adjacent_to_symbol is True:
                    if index not in index_gears.keys():
                        index_gears[index] = []
                    index_gears[index].append(int(number))
                is_adjacent_to_symbol = False
                number = ""

    for index, gears_list in index_gears.items():
        if len(gears_list) == 2:
            gear_ratio = gears_list[0] * gears_list[1]
            gear_ratios.append(gear_ratio)

    return sum(gear_ratios)


def __main__():
    puzzle_input = get_puzzle_input("03/input.txt")

    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    __main__()
