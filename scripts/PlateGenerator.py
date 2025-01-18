from PIL import Image, ImageDraw, ImageFont
import os
import random

# Paths and directories
TEMPLATE_PATH = r"C:\Users\camie\Documents\lege kentekenplaat.webp"  # Path to your blank plate image
OUTPUT_DIR = r"C:\Users\camie\OneDrive\school\hanze\FraudDetectionCjib\generated_plates"
FONT_PATH = "arial.ttf"  # Path to your font file

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    print(f"Created output directory: {OUTPUT_DIR}")

# Generate random Dutch number plates
def generate_random_plate():
    """Generate a random Dutch number plate."""
    formats = [
        "{0}{1}-{2}{3}{4}-{5}",  # Example: XX-999-X
        "{0}-{1}{2}-{3}{4}{5}",  # Example: 9-X-999
    ]
    chosen_format = random.choice(formats)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    return chosen_format.format(
        random.choice(letters),
        random.choice(letters),
        random.choice(digits),
        random.choice(digits),
        random.choice(digits),
        random.choice(letters),
    )

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
        if random.randint(1, 50) <= 10:  # 10% chance
            print("Adding black box to cover 'NL'")
            # Define the black box position (adjust coordinates to cover the "NL" part)
            box_position = [(100, 250), (180, 460)]  # Adjust these values to fit "NL"
            draw.rectangle(box_position, fill="black")

        # Save the generated plate
        template.save(output_path)
        print(f"Generated plate: {output_path}")

    except Exception as e:
        print(f"Error generating plate {plate_text}: {e}")

def generate_multiple_plates(count):
    """Generate multiple number plates."""
    print(f"Generating {count} plates...")
    for i in range(count):
        plate_text = generate_random_plate()
        output_path = os.path.join(OUTPUT_DIR, f"plate_{i+1}.png")  # Save each plate with a unique name
        create_number_plate(plate_text, output_path)
    print("Plate generation completed!")

# Main execution
if __name__ == "__main__":
    print("Starting plate generation...")
    generate_multiple_plates(100)  # Generate 100 plates
    print("All plates have been generated!")
