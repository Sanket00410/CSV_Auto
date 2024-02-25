import csv
import os

def extract_info_from_csv(input_csv_filename, output_csv_filename, names_to_search):
    extracted_info = []

    with open(input_csv_filename, 'r', newline='') as input_csv_file:
        reader = csv.DictReader(input_csv_file)

        for row in reader:
            for name in names_to_search:
                if any(name.lower() in value.lower() for value in row.values()):
                    extracted_info.append(row)
                    break  # Break out of the inner loop once a match is found for the current name

    if extracted_info:
        append_mode = 'a' if os.path.exists(output_csv_filename) else 'w'
        with open(output_csv_filename, append_mode, newline='') as output_csv_file:
            writer = csv.DictWriter(output_csv_file, fieldnames=extracted_info[0].keys())
            if append_mode == 'w':
                writer.writeheader()  # Write header only if the file is newly created
            writer.writerows(extracted_info)

        print(f"Extracted information saved to {output_csv_filename} successfully.")
    else:
        print("No matching information found.")

if __name__ == "__main__":
    input_csv_filename = input("Enter the input CSV filename: ")
    output_csv_filename = input("Enter the output CSV filename: ")
    names_to_search = input("Enter names to search separated by commas: ").split(',')

    extract_info_from_csv(input_csv_filename, output_csv_filename, names_to_search)
