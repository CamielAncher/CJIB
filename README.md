# 🚗 Fraud Detection with Plate Recognition

Welcome to the **Fraud Detection with Plate Recognition** project! This private repository is designed to identify potential fraudulent license plates by analyzing missing "NL" identifiers. The project leverages Azure services and Python to streamline detection and reporting workflows.

---

## 📖 Overview

This project focuses on:

- **Analyzing license plates** stored in Azure Blob Storage.
- Using **Azure Computer Vision** to extract text from license plates.
- Detecting anomalies, specifically missing "NL" identifiers.
- Generating **mock license plates** for testing edge cases.

This serves as the foundation for exploring fraud detection techniques using cloud and AI technologies, with plans for future enhancements.

---

## 🛠️ Features

### Current Capabilities
- **Missing "NL" Detection:** Automatically flags plates without the "NL" identifier.
- **Batch Processing:** Analyze up to as many license plate images in a single run as you want to pay for.
- **Custom Plate Generation:** Simulate license plate images with anomalies for testing.
- **Simple Reporting:** Flagged anomalies are logged for further inspection.
- **Azure Integration:** Seamless integration with Azure Blob Storage and Computer Vision API.

### Future Enhancements
- Advanced fraud detection for tampered or altered plates.
- Machine learning models for detecting patterns.
- Real-time processing for live plate analysis.
- Enhanced reporting with visual dashboards.

---

## 🚀 Getting Started

### Prerequisites
Before running the project, ensure you have:

1. **Python 3.13 or higher** installed.
2. An Azure account with:
   - **Blob Storage** set up for storing license plate images.
   - **Computer Vision API** enabled for text extraction.
3. Required Python libraries installed (listed in `requirements.txt`).

### Setup
1. Clone this repository to your local environment.
2. Install the required dependencies using the `requirements.txt` file.
3. Configure Azure settings by updating the following variables in the scripts:
   - `STORAGE_ACCOUNT_URL`
   - `CONTAINER_NAME`
   - `subscription_key`
   - `endpoint`

---

## 🔧 Usage

### Detect Missing "NL"
- Run the `combined.py` script to analyze license plates stored in Azure Blob Storage.
- The script will:
  1. Analyze images and extract text.
  2. Detect plates missing the "NL" identifier.
  3. Save flagged cases to `Output/Further inspection.txt`.

### Generate Test Plates
- Use the `PlateGenerator.py` script to create simulated license plate images.
- Generated plates will be saved in the `Output/generated plates/` directory.

### Fetch License Plate Data
- Run the `PlateFetcher.py` script to retrieve real-world license plate data from the RDW Open Data API.
- Formatted plates will be saved in `Output/formatted_kentekens.csv`.

---

## 🧪 Testing & Validation

### Current Detection Logic
- The system scans license plates and flags cases where the "NL" identifier is missing.
- All flagged anomalies are logged in `Output/Further inspection.txt`.

### Testing Scenarios
- **Simulated edge cases:** Plates missing or obscuring the "NL" identifier.
- **Randomized data:** Diverse test scenarios using generated plates.

---

## 🔒 Security Notes

- This repository is private. Do not share or publish it publicly.
- Avoid hardcoding sensitive credentials. Use environment variables or tools like **Azure Key Vault**.
- Regularly rotate your API keys to maintain security.

---

## 📝 License

This repository is private and intended for internal use only. **Unauthorized distribution or replication is strictly prohibited.**

---
