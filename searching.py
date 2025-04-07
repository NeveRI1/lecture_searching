import os

from lecture_08.lecture_searching.generators import unordered_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in ('unordered_numbers','ordered_numbers','dna_sequence'):
        return None

    file_path = os.path.join(cwd_path, file_name)


def main():
    with open('sequential.json', 'r') as file:
        data = json.load(file)
        ordered_numbers = data['ordered_numbers']

    target = 15

    result = binary_search(ordered_numbers, target)

    if result is not None:
        print(f"Cislo {target} nalezeno na indexu {result}.")
    else:
        print(f"Cislo {target} nebylo nalezeno.")

if __name__ == '__main__':
    main()

def pattern_search(seq, pattern):

    indices = []
    count = 0

    idx = 0

    while idx < len(seq):
        if seq(idx) == number:
            indices.append(idx)
            count += 1
        idx += 1

def binary_search(ordered_numbers, target):
    left, right = 0, len(ordered_numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if ordered_numbers[mid] == target:
            return mid
        elif ordered_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None
