from azure.storage.blob import BlobServiceClient

# Public Blob Storage account URL (only the account URL, without the container name)
STORAGE_ACCOUNT_URL = "https://cjib.blob.core.windows.net"
CONTAINER_NAME = "number-plate-pictures"

# Initialize Blob Service Client for a public container (no credentials needed)
blob_service_client = BlobServiceClient(account_url=STORAGE_ACCOUNT_URL)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def list_blob_urls():
    """List all blob URLs in a public container."""
    print(f"Listing blob URLs in public container '{CONTAINER_NAME}':")
    blob_list = container_client.list_blobs()

    for blob in blob_list:
        # Construct the public URL for each blob
        blob_url = f"{STORAGE_ACCOUNT_URL}/{CONTAINER_NAME}/{blob.name}"
        print(f"- Blob Name: {blob.name}")
        print(f"  Blob URL: {blob_url}\n")

if __name__ == "__main__":
    list_blob_urls()
