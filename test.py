from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import os
from PIL import Image

# Azure subscription details
subscription_key = "AkI53NcuEfojIqy7nIyHVQZSsCS0WkamgX13k27PRtq2mKNdYWv7JQQJ99ALACYeBjFXJ3w3AAAAACOGFj1E"
endpoint = "https://visionbot1.cognitiveservices.azure.com/"

# Authenticate client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# Analyze image with OCR
def extract_text_from_image(image_path): r"C:\Users\camie\OneDrive\school\hanze\FraudDetectionCjib\2048x1152.jpg"
    """
    Extracts text from an image using Azure Computer Vision OCR.
    """
    try:
        with open(image_path, "rb") as image_stream:
            ocr_result = computervision_client.recognize_printed_text_in_stream(image_stream, language="en")

        # Parse and return the detected text
        detected_text = []
        for region in ocr_result.regions:
            for line in region.lines:
                line_text = " ".join([word.text for word in line.words])
                detected_text.append(line_text)

        return detected_text

    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Path to your uploaded photo
    image_path = r"C:\Users\Camie\OneDrive\school\hanze\2048x1152.jpg"  # Use raw string for Windows paths

    # Extract text
    if os.path.exists(image_path):
        detected_text = extract_text_from_image(image_path)
        print("Detected text:")
        print("\n".join(detected_text))
    else:
        print("Image file not found because i dont like you(remeber to change this).")

#testing to see changes