from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Azure subscription details
subscription_key = "AkI53NcuEfojIqy7nIyHVQZSsCS0WkamgX13k27PRtq2mKNdYWv7JQQJ99ALACYeBjFXJ3w3AAAAACOGFj1E"
endpoint = "https://visionbot1.cognitiveservices.azure.com/"

# Authenticate client
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Image path
image_path = r"C:\Users\Camie\OneDrive\Pictures\hanze\2048x1152.jpg"

# Send the image to Azure and print the OCR response
try:
    with open(image_path, "rb") as image_stream:
        ocr_result = computervision_client.recognize_printed_text_in_stream(image_stream, language="en")

    # Print the OCR response
    for region in ocr_result.regions:
        for line in region.lines:
            print(" ".join([word.text for word in line.words]))

except Exception as e:
    print(f"Error: {e}")
