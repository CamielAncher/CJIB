from PIL import Image, ImageDraw, ImageFont
import os
import random
import csv

# Paths and directories
TEMPLATE_PATH = r""  # Path to your blank plate image
OUTPUT_DIR = r""
FONT_PATH = "arial.ttf"  # Path to your font file
CSV_FILE_PATH = r""  # Path to the CSV file containing plates

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    print(f"Created output directory: {OUTPUT_DIR}")

def create_number_plate(plate_text, output_path):
    """Create a number plate with the given text."""
    try:
        # Open the blank template image
        template = Image.open(TEMPLATE_PATH)
        draw = ImageDraw.Draw(template)

        # Use default font if no custom font file is available
        try:
            font = ImageFont.truetype(FONT_PATH, 190)  # Adjust font size as needed
        except IOError:
            print(f"Font file not found at {FONT_PATH}. Using default font.")
            font = ImageFont.load_default()

        # Define text position and color
        text_position = (215, 255)  # Adjust based on your template
        text_color = "black"  # Color of the text

        # Draw the text onto the template
        draw.text(text_position, plate_text, fill=text_color, font=font)

        # Randomly decide if a black box should cover "NL"
        if random.randint(1, 1000) <= 10:  # 1% chance
            print(f"Adding black box to cover 'NL' for plate {plate_text}")
            # Define the black box position (adjust coordinates to cover the "NL" part)
            box_position = [(100, 250), (180, 460)]  # Adjust these values to fit "NL"
            draw.rectangle(box_position, fill="black")

        # Save the generated plate
        template.save(output_path)
        print(f"Generated plate: {output_path}")

    except Exception as e:
        print(f"Error generating plate {plate_text}: {e}")

def generate_plates_from_csv(csv_file_path):
    """Generate plates based on data from a CSV file."""
    try:
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row if present
            i = 9744
            print(f"Generating plates from CSV: {csv_file_path}")
            for i, row in enumerate(reader):
                plate_text = row[0]  # Assuming the number plate is in the first column
                output_path = os.path.join(OUTPUT_DIR, f"plate_{i+1}.png")
                create_number_plate(plate_text, output_path)

        print("Plate generation completed!")
    except Exception as e:
        print(f"Error reading CSV file {csv_file_path}: {e}")

# Main execution
if __name__ == "__main__":
    print("Starting plate generation from CSV...")
    generate_plates_from_csv(CSV_FILE_PATH)
    print("All plates have been generated!")
