from pathlib import Path
import json
import random
import time
import matplotlib.pyplot as plt

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

def pattern_search(sequence, pattern):
    positions = set()
    n = len(sequence)
    m = len(pattern)

    for i in range(n - m + 1):
        if sequence[i:i + m] == pattern:
            positions.add(i)

    return positions

def generate_data(size):
    data = [random.randint(1, 10000) for _ in range(size)]
    return data, sorted(data)

def measure_time():
    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []

    for size in sizes:
        data, sorted_data = generate_data(size)
        target = data[-1]

        start = time.time()
        linear_search(data, target)
        linear_times.append(time.time() - start)

        start = time.time()
        binary_search(sorted_data, target)
        binary_times.append(time.time() - start)

    return sizes, linear_times, binary_times

def plot_results(sizes, linear_times, binary_times):
    plt.plot(sizes, linear_times, label="Linear search")
    plt.plot(sizes, binary_times, label="Binary search")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas běhu (s)")
    plt.title("Porovnání vyhledávání")

    plt.legend()
    plt.grid()
    plt.show()

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Unordered:", sequential_data)

    ordered_data = read_data("sequential.json", "ordered_numbers")
    print("Ordered:", ordered_data)

    dna_sequence = read_data("sequential.json", "dna_sequence")
    print("DNA loaded")

    print("\nLinear search:")
    print(linear_search(sequential_data, 5))

    print("\nBinary search:")
    print(binary_search(ordered_data, 5))

    print("\nPattern search:")
    pattern = "ATA"
    print(pattern_search(dna_sequence, pattern))

    sizes, linear_times, binary_times = measure_time()
    plot_results(sizes, linear_times, binary_times)

if __name__ == "__main__":
    main()
