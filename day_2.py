
def parse_input(filepath:str) -> list[str]:

    """
    The input seems to be one long line, which I think we want to be a list of ranges.
    
    We can then hand that to another function to use. 
    
    :param file_path: 
    :return: 
    """

    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()

    # now we need to parse the csv values into a list

    range_list = [item.strip() for item in data.split(',') if item.strip()]

    return range_list

def find_invalid_ids(range_list: list[str]) -> list:
    """
    Produce a list of items that are invalid between the given ranges

    :param range_list:
    :return:
    """

    # let's try the naive version first where we brute force this.   is this a good idea?

    repeated_nums = []

    for item in range_list:

        start_val, end_val  = map(int, item.split('-'))
        # print(f'{start_val=}{end_val=}')

        # always a warning sign, but now I am doing another loop between the numbers and looking for a match on somehting

        for num in range(start_val, end_val+1):
            # print(num)
            str_num = str(num)

            # if the number has an odd number it cannot be made up of digits repeated twice
            if len(str_num) % 2 == 0:
                mid = len(str_num) // 2

                left = str_num[:mid]
                right = str_num[mid:]

                if left == right:
                    # we have a repeating sequence
                    repeated_nums.append(str_num)


    return repeated_nums


def sum_invalid_ids(repeated_nums: list[str]) -> int:

    sum_val = sum(map(int, repeated_nums))

    return sum_val

def find_invalid_ids_part_two(range_list: list[str]) -> list:
    """
    Produce a list of items that are invalid between the given ranges

    :param range_list:
    :return:
    """

    # let's try the naive version first where we brute force this.   is this a good idea?

    repeated_nums = []

    for item in range_list:

        start_val, end_val  = map(int, item.split('-'))
        # print(f'{start_val=}{end_val=}')

        # always a warning sign, but now I am doing another loop between the numbers and looking for a match on somehting

        for num in range(start_val, end_val+1):
            # print(num)
            str_num = str(num)

            # now we need to split it into component parts until the mid point, not just at the mid point
            mid = len(str_num) // 2

            for i in range(1, mid+1):
                # print(f"now looping up ")

                #lets chunk into sizes of
                chunks = [str_num[j:j + i] for j in range(0, len(str_num), i)]

                # print(f"{chunks=}")

                if len(set(chunks)) <= 1:
                    # print(f"found a match: {str_num}")
                    repeated_nums.append(str_num)


    return  list(set(repeated_nums))

if __name__ == "__main__":
    range_list = parse_input("data/day_2_example_data.txt")
    print(f"{range_list=}")
    invalid_id_list = find_invalid_ids(range_list)
    print(f"{invalid_id_list=}")

    sum_of_invalid_ids = sum_invalid_ids(invalid_id_list)
    print(f"{sum_of_invalid_ids=}")

    range_list_2 = parse_input("data/day_2_real_data.txt")
    invalid_id_list_2 = find_invalid_ids_part_two(range_list_2)
    print(f"{invalid_id_list_2=}")
    sum_of_invalid_ids_2 = sum_invalid_ids(invalid_id_list_2)
    print(f"{sum_of_invalid_ids_2=}")


