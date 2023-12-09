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
    games = []
    for _, row in enumerate(puzzle_input):
        left, right = row.split("|")
        left = list(map(int, left.split()[2:]))
        right = list(map(int, right.split()))
        game = {"winning_numbers": left, "numbers": right}
        games.append(game)
    return games


def part_1(puzzle_input):
    games = process_input(puzzle_input)
    score = 0

    for game in games:
        set1 = set(game["winning_numbers"])
        set2 = set(game["numbers"])
        winning_numbers = set1.intersection(set2)

        if len(winning_numbers) >= 1:
            score += 2 ** (len(winning_numbers) - 1)

    return score


def part_2(puzzle_input):
    game_matching_numbers = {}
    games = process_input(puzzle_input)
    all_scratchcards = {}

    for index, game in enumerate(games):
        set1 = set(game["winning_numbers"])
        set2 = set(game["numbers"])
        winning_numbers = set1.intersection(set2)
        game_matching_numbers[index + 1] = len(winning_numbers)

    for i in range(len(games)):
        all_scratchcards[i + 1] = 1

    for index, cards in all_scratchcards.items():
        for i in range(cards):
            for j in range(index + 1, index + 1 + game_matching_numbers[index]):
                all_scratchcards[j] += 1

    scratchcard_count = 0
    for count in all_scratchcards.values():
        scratchcard_count += count

    return scratchcard_count


def __main__():
    puzzle_input = get_puzzle_input("04/input.txt")

    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    __main__()
