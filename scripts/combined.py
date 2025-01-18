from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.storage.blob import BlobServiceClient

# Azure details
STORAGE_ACCOUNT_URL = "https://cjib.blob.core.windows.net"
CONTAINER_NAME = "number-plate-pictures"
subscription_key = "AkI53NcuEfojIqy7nIyHVQZSsCS0WkamgX13k27PRtq2mKNdYWv7JQQJ99ALACYeBjFXJ3w3AAAAACOGFj1E"
endpoint = "https://visionbot1.cognitiveservices.azure.com/"

# Initialize
blob_service_client = BlobServiceClient(account_url=STORAGE_ACCOUNT_URL)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def list_blob_urls(max_pictures=10):
    """List a limited number of blob URLs in a public container and analyze them with Azure Vision API."""
    print(f"Processing up to {max_pictures} blob(s) in public container '{CONTAINER_NAME}':")
    blob_list = container_client.list_blobs()

    # Counter for processed blobs
    count = 0
    fraudCount = 0

    for blob in blob_list:
        if count >= max_pictures:
            break  # Stop after processing the specified number of pictures

        # Construct the public URL for each blob
        blob_url = f"{STORAGE_ACCOUNT_URL}/{CONTAINER_NAME}/{blob.name}"
        print(f"Processing blob: {blob_url}")

        try:
            # Analyze the image using the Vision API
            read_response = computervision_client.read(blob_url, raw=True)

            # Handle the async response
            operation_location = read_response.headers["Operation-Location"]
            operation_id = operation_location.split("/")[-1]

            # Poll the Vision API for the result
            while True:
                result = computervision_client.get_read_result(operation_id)
                if result.status not in ["notStarted", "running"]:
                    break

            detected_text = ""
            if result.status == "succeeded":
                for page in result.analyze_result.read_results:
                    for line in page.lines:
                        detected_text += line.text + " "

            # Check if "NL" is present in the detected text
            if "NL" not in detected_text.strip():
                print("further inspection needed")
                with open(r"C:\Users\camie\OneDrive\school\hanze\FraudDetectionCjib\docs\Further inspection.txt", "a") as file:
                    file.write(f"{blob_url}\n")
                fraudCount += 1
            
            else:
                print(f"detected: {detected_text.strip()}")
            

           
        except Exception as e:
            print(f"Error processing blob '{blob.name}': {e}")

        # Increment the counter
        count += 1

    print(f"Processed {count} blob(s).")
    print(f"Number of possible fraudulent activities detected: {fraudCount}")

if __name__ == "__main__":
    # Set the number of blobs to process
    list_blob_urls(max_pictures=10)  # Change this value as needed
