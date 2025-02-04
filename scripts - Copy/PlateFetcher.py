import csv
import requests
import random

# Paths
OUTPUT_CSV_PATH = r""  # Path to save the CSV
API_URL = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
BATCH_SIZE = 30  # Number of plates per batch
TOTAL_PLATES = 60000  # Total number of plates to generate
API_TOTAL_COUNT = 16000000  # Estimated total number of plates in the API dataset

def randomize_hyphen(plate_text):
    """
    Randomly place hyphens in the plate text.
    """
    formats = [
        "{0}{1}-{2}{3}-{4}{5}",    # Example: 12-34-56
        "{0}{1}-{2}{3}{4}-{5}",    # Example: 12-345-6
        "{0}-{1}{2}-{3}{4}{5}",    # Example: 1-23-456
        "{0}{1}{2}-{3}{4}-{5}",    # Example: 123-45-6
    ]
    chosen_format = random.choice(formats)
    return chosen_format.format(*plate_text)

def fetch_data_from_api(offset, limit):
    """
    Fetch a batch of number plates from the API.
    """
    query = f"?$query=SELECT kenteken LIMIT {limit} OFFSET {offset}"
    response = requests.get(API_URL + query)
    if response.status_code == 200:
        data = response.json()
        return [item["kenteken"] for item in data if "kenteken" in item]
    else:
        print(f"Error fetching data from API: {response.status_code}")
        return []

def generate_csv_from_api(output_path, total_plates, batch_size, total_api_count):
    """
    Generate a CSV file with number plates based on real API data,
    randomizing the hyphen position and ensuring offsets for diversity.
    """
    try:
        with open(output_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Formatted Kenteken"])  # Header row

            total_batches = total_plates // batch_size
            print(f"Generating {total_plates} plates in {total_batches} batches...")

            for batch in range(total_batches):
                # Calculate a random offset within the total API dataset
                max_offset = max(0, total_api_count - batch_size)  # Ensure we don’t exceed dataset bounds
                offset = random.randint(0, max_offset)
                print(f"Fetching batch {batch + 1} with random offset {offset}...")

                # Fetch data from the API
                plates = fetch_data_from_api(offset, batch_size)

                # Randomize hyphen placement and write to CSV
                for plate in plates:
                    randomized_plate = randomize_hyphen(plate)
                    writer.writerow([randomized_plate])

            print(f"CSV generation completed! File saved at: {output_path}")

    except Exception as e:
        print(f"Error generating CSV file: {e}")

# Main execution
if __name__ == "__main__":
    print("Starting CSV generation...")
    generate_csv_from_api(OUTPUT_CSV_PATH, TOTAL_PLATES, BATCH_SIZE, API_TOTAL_COUNT)
