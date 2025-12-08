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
                if item > first_digit:
                    first_digit = item
                    second_digit = 0
                elif item > second_digit:
                    second_digit = item

            # print(f"So far: {first_digit=} {second_digit=}")

        print(f"Final: {first_digit=} {second_digit=}")

        cum_sum += int(''.join([str(first_digit), str(second_digit)]))

    return cum_sum



def calculate_total_output_joltage_bank(joltage_list: list[str], bank_size:int = 12) -> int:

    cum_sum = 0

    for joltages in joltage_list:
        # The result will be a list of characters (digits) that form the max joltage
        max_joltage_digits = []
        
        # 'values' is the list of digits as characters
        joltage_values = list(joltages)
        values_len = len(joltage_values)
        
        # 'n_to_select' is the number of digits we must select
        n_to_select = bank_size
        
        # The index in the original 'values' list where the search for the next digit must start
        start_search_index = 0
        
        # The greedy algorithm: Iterate for the number of digits we need to select (12 times)
        for i in range(n_to_select):
            
            # --- DEFINE THE SEARCH WINDOW END ---
            # The search for the i-th digit must end at the latest possible position
            # that still leaves (n_to_select - 1 - i) more digits to be chosen.
            # Example (i=0, select 12): Must leave 11. End search at index (len - 11 - 1) + 1 = len - 11
            # end_search_index = values_len - (n_to_select - i) + 1 
            # Simplified: end_search_index is the index of the last element we can consider + 1
            # Index of the last possible choice: values_len - (n_to_select - i) 
            end_search_index = values_len - (n_to_select - 1 - i)
            
            # --- FIND THE MAX DIGIT IN THE CURRENT WINDOW ---
            max_digit = -1 
            max_digit_index = -1
            
            # Search the window for the largest available digit
            for j in range(start_search_index, end_search_index):
                current_digit = int(joltage_values[j])
                
                # We need to find the largest digit and the *earliest* index where it occurs.
                if current_digit > max_digit:
                    max_digit = current_digit
                    max_digit_index = j
                    
                    # Optimization: If we find a '9', it's the absolute best, 
                    # so we can stop searching this window.
                    if max_digit == 9:
                        break

            # --- SELECT THE MAX DIGIT AND UPDATE START INDEX ---
            
            # Append the largest digit found in the window to the result
            max_joltage_digits.append(joltage_values[max_digit_index])
            
            # The search for the *next* digit must start immediately *after* the one we just selected.
            start_search_index = max_digit_index + 1
        
        # After selecting all 12 digits, form the number and add it to the cumulative sum
        joltage_str = "".join(max_joltage_digits)
        print(f"Bank: {joltages} -> Max Joltage: {joltage_str}")
        cum_sum += int(joltage_str)

    return cum_sum


def calculate_total_output_joltage_bank_early_exit(joltage_list: list[str], bank_size:int = 12) -> int:

    cum_sum = 0

    for joltages in joltage_list:
        # The result will be a list of characters (digits) that form the max joltage
        max_joltage_digits = []
        
        # 'values' is the list of digits as characters
        joltage_values = list(joltages)
        values_len = len(joltage_values)
        
        # 'n_to_select' is the number of digits we must select
        n_to_select = bank_size
        
        # The index in the original 'values' list where the search for the next digit must start
        start_search_index = 0
        
        # The greedy algorithm: Iterate for the number of digits we need to select (12 times)
        for i in range(n_to_select):
            # ----- EARLY EXIT: MUST TAKE ALL REMAINING DIGITS -----
            # If the number of digits left equals the number of slots left to fill,
            # we are forced to take all remaining digits in order.
            remaining_digits = values_len - start_search_index
            remaining_slots = n_to_select - i
            if remaining_digits == remaining_slots:
                max_joltage_digits.extend(joltage_values[start_search_index:])
                break
            
            # --- DEFINE THE SEARCH WINDOW END ---
            # The search for the i-th digit must end at the latest possible position
            # that still leaves (n_to_select - 1 - i) more digits to be chosen.
            end_search_index = values_len - (n_to_select - 1 - i)
            
            # --- FIND THE MAX DIGIT IN THE CURRENT WINDOW ---
            max_digit = -1 
            max_digit_index = -1
            
            # Search the window for the largest available digit
            for j in range(start_search_index, end_search_index):
                current_digit = int(joltage_values[j])
                
                # We need to find the largest digit and the *earliest* index where it occurs.
                if current_digit > max_digit:
                    max_digit = current_digit
                    max_digit_index = j
                    
                    # Optimization: If we find a '9', it's the absolute best, 
                    # so we can stop searching this window.
                    if max_digit == 9:
                        break

            # --- SELECT THE MAX DIGIT AND UPDATE START INDEX ---
            
            # Append the largest digit found in the window to the result
            max_joltage_digits.append(joltage_values[max_digit_index])
            
            # The search for the *next* digit must start immediately *after* the one we just selected.
            start_search_index = max_digit_index + 1
        
        # After selecting all 12 digits, form the number and add it to the cumulative sum
        joltage_str = "".join(max_joltage_digits)
        print(f"Bank: {joltages} -> Max Joltage: {joltage_str}")
        cum_sum += int(joltage_str)

    return cum_sum


if __name__ == "__main__":
    # joltage_list = parse_input("data/day_3_example_data.txt")
    # print(f"{joltage_list=}")
    # total_output_joltage_example = calculate_total_output_joltage(joltage_list)
    # print(f"{total_output_joltage_example=}")

    # joltage_list = parse_input("data/day_3_real_data.txt")
    # print(f"{joltage_list=}")
    # total_output_joltage_real = calculate_total_output_joltage(joltage_list)
    # print(f"{total_output_joltage_real=}")

    joltage_list = parse_input("data/day_3_real_data.txt")
    print(f"{joltage_list=}")
    total_output_joltage_bank_example = calculate_total_output_joltage_bank_early_exit(joltage_list)
    print(f"{total_output_joltage_bank_example=}")

