from typing import List

def parse_input(filepath: str) -> list:

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return lines




def calculate_crossings_over_zero(instruction_set: List[str], starting_pos: int = 50) -> int:
    """
    Count how many times any single click causes the dial to land on 0.

    The dial:
      - Has positions 0..99 (mod 100)
      - Starts at `starting_pos`
      - Each instruction is like "R48" or "L5":
          - 'R' = move toward higher numbers
          - 'L' = move toward lower numbers
          - the number is the count of clicks

    For each instruction, we count all clicks during that rotation
    whose resulting position is exactly 0.
    """
    current_pos = starting_pos
    number_of_zero_passes = 0

    for rotation in instruction_set:
        rotation = rotation.strip()

        if not (0 <= current_pos <= 99):
            raise ValueError(f"Error: current_pos {current_pos} out of range 0..99")

        rotation_direction = rotation[0]
        clicks = int(rotation[1:])  # number of single-click steps in this rotation

        # Count how many of those clicks land on 0
        if rotation_direction == 'R':
            # positions visited: (current_pos + 1)..(current_pos + clicks) mod 100
            first_k = (100 - current_pos) % 100
            if first_k == 0:
                first_k = 100
        elif rotation_direction == 'L':
            # positions visited: (current_pos - 1)..(current_pos - clicks) mod 100
            first_k = current_pos % 100
            if first_k == 0:
                first_k = 100
        else:
            raise ValueError(f"Bad direction {rotation_direction!r}")

        if first_k <= clicks:
            number_of_zero_passes += 1 + (clicks - first_k) // 100

        # Apply the rotation to update the dial position
        if rotation_direction == 'R':
            current_pos = (current_pos + clicks) % 100
        else:  # 'L'
            current_pos = (current_pos - clicks) % 100

    return number_of_zero_passes



def calculate_door_password(instruction_set: list, starting_pos: int = 50) -> int:
    """
    "Due to new security protocols, the password is locked in the safe below.
    Please see the attached document for the new combination."

    The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order.
    As you turn the dial, it makes a small click noise as it reaches each number.

    The attached document (your puzzle input) contains a sequence of rotations, one per line,
    which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

    So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19.
    After that, a rotation of L19 would cause it to point at 0.

    Because the dial is a circle, turning the dial left from 0 one click makes it point at 99.
    Similarly, turning the dial right from 99 one click makes it point at 0.

    So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95.
    After that, a rotation of R5 could cause it to point at 0.

    The dial starts by pointing at 50.

    You could follow the instructions, but your recent required official North Pole secret entrance security
    training seminar taught you that the safe is actually a decoy. The actual password is the number of times
    the dial is left pointing at 0 after any rotation in the sequence.

    :param instruction_set:
    :return: int: represents the number of times the dial was pointing at 0
    """

    current_pos = starting_pos
    number_of_zero_visits = 0

    for rotation in instruction_set:

        finish_pos = 0

        # parse the instruction, we expect this to have a letter for direction, then a number of clicks.

        rotation_direction = rotation[0]
        rotation_value = int(rotation[1:])

        # oops, there is data showing it is "legal" to spin the dial more than one rotation.
        # hack here is... when you do, only the fractions of a spin matter
        rotation_value = rotation_value % 100

        # we need to see how many full spins we see go "past" zero

        if rotation_direction == "L":
            # we are going DOWN numbers ( assuming the dial is printed in clockwise fashion )
            new_pos = current_pos - rotation_value

            # remember: "minus minus" is plus
            finish_pos = new_pos if new_pos >= 0 else 100 + new_pos

        elif rotation_direction == "R":
            # we are going UP numbers ( assuming the dial is printed in clockwise fashion )
            new_pos = current_pos + rotation_value

            finish_pos = new_pos if new_pos < 100 else new_pos - 100
        else:
            raise ValueError(f"Invalid rotation instruction character {rotation_direction}")

        if finish_pos == 0:
            number_of_zero_visits += 1

        current_pos = finish_pos

    return number_of_zero_visits


if __name__ == "__main__":
    input_data = parse_input("data/day_one_real_data.txt")
    answer_part_1 = calculate_door_password(input_data)
    print(f"Part One: {answer_part_1}")

    answer_part_2 = calculate_crossings_over_zero(instruction_set=input_data)
    print(f"Part Two: {answer_part_2}")



