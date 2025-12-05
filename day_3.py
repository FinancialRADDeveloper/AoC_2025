def parse_input(filepath: str) -> list[str]:
    """
    The input seems to be one long line, which I think we want to be a list of ranges.

    We can then hand that to another function to use.

    :param filepath:
    :return:
    """

    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data = [item.strip() for item in data]


    return data


def calculate_total_output_joltage(joltage_list: list[str]) -> int:


    cum_sum = 0

    for bank in joltage_list:

        first_digit = 0
        second_digit = 0

        # cannot just reverse sort and take the first two values as the order is important
        values =  list(map(int, bank))

        values_len = len(values) - 1

        for i, item in enumerate(values):

            if i == values_len:
                if item > second_digit:
                    second_digit = item
            else:
                if item >= first_digit:
                    first_digit = item
                    second_digit = 0
                elif item >= second_digit:
                    second_digit = item

            print(f"So far: {first_digit=} {second_digit=}")

        print(f"Final: {first_digit=} {second_digit=}")

        cum_sum += int(''.join([str(first_digit), str(second_digit)]))

    return cum_sum


if __name__ == "__main__":
    joltage_list = parse_input("data/day_3_example_data.txt")
    print(f"{joltage_list=}")
    total_output_joltage = calculate_total_output_joltage(joltage_list)
    print(f"{total_output_joltage=}")
