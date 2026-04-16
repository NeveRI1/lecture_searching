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

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

if __name__ == "__main__":
    main()
