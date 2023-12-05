def get_puzzle_input(file_path):
    try:
        with open(file_path, "r") as file:
            puzzle_input = file.readlines()

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print("An error occurred:", e)

    return puzzle_input


def find_first_number_in_string(string):
    numbers = "0123456789"

    for character in string:
        if character in numbers:
            return character


def part_1(puzzle_input):
    calibration_values = []

    for line in puzzle_input:
        first_number = find_first_number_in_string(line)
        last_number = find_first_number_in_string(line[::-1])

        calibration_values.append(first_number + last_number)

    calibration_values_sum = 0

    for value in calibration_values:
        calibration_values_sum += int(value)

    return calibration_values_sum


def part_2(puzzle_input):
    numbers_as_text = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    calibration_values = []

    for line in puzzle_input:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                substring = line[i:j]
                if substring in numbers_as_text:
                    if substring in numbers_as_text:
                        line = line[:i] + numbers_as_text[substring] + line[j:]
                        break

        first_number = find_first_number_in_string(line)
        last_number = find_first_number_in_string(line[::-1])

        calibration_values.append(first_number + last_number)

    calibration_values_sum = 0

    for value in calibration_values:
        calibration_values_sum += int(value)

    return calibration_values_sum


def __main__():
    puzzle_input = get_puzzle_input("01/input.txt")

    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    __main__()
