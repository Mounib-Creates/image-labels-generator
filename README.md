# image-labels-generator
A serverless image labeling tool using AWS S3, Rekognition, and AWS CLI.

# 🏷️ Image Labels Generator

A simple cloud-based tool that automatically labels images using **Amazon Rekognition**. Images are uploaded to **Amazon S3**, analyzed using **AWS CLI**, and the labels are returned in a structured format.

## 📌 Tools Used

- **Amazon S3** – for image storage
- **Amazon Rekognition** – for image labeling
- **AWS CLI** – for interacting with AWS services
- **Bash Scripts** – for automation

## ⚙️ How It Works

1. Upload an image to S3 using AWS CLI
2. Call Rekognition to detect labels
3. Output labels in JSON format
4. (Optional) Parse or visualize the output

## 🧪 Example Output

```json
{
  "Labels": [
    {
      "Name": "Dog",
      "Confidence": 98.7
    },
    {
      "Name": "Pet",
      "Confidence": 96.3
    }
  ]
}
