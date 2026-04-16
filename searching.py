from pathlib import Path
import json

def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    allowed_fields = ["unordered_numbers", "ordered_numbers", "dna_sequence"]

    if field not in allowed_fields:
        return None

    return data.get(field)

def linear_search(sequence, target):
    positions = []

    for i in range(len(sequence)):
        if sequence[i] == target:
            positions.append(i)

    return {
        "positions": positions,
        "count": len(positions)
    }

def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Unordered data:", sequential_data)

    target_linear = 31
    result = linear_search(sequential_data, target_linear)

    print("\nLinear search:")
    print("Hledané číslo:", target_linear)
    print("Pozice:", result["positions"])
    print("Počet výskytů:", result["count"])

    ordered_data = read_data("sequential.json", "ordered_numbers")
    print("\nOrdered data:", ordered_data)

    target_binary = 14
    index = binary_search(ordered_data, target_binary)

    print("\nBinary search:")
    print("Hledané číslo:", target_binary)
    print("Index:", index)

if __name__ == "__main__":
    main()
