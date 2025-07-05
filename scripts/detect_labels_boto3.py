import boto3
import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('--bucket', required=True, help='S3 Bucket Name')
parser.add_argument('--file', required=True, help='Image file name in S3')
parser.add_argument('--region', default='eu-central-1', help='AWS Region')
args = parser.parse_args()

rekognition = boto3.client('rekognition', region_name=args.region)

response = rekognition.detect_labels(
    Image={'S3Object': {'Bucket': args.bucket, 'Name': args.file}},
    MaxLabels=10,
    MinConfidence=70
)

output_path = f'./output/labels_{os.path.splitext(args.file)[0]}.json'
with open(output_path, 'w') as f:
    json.dump(response['Labels'], f, indent=2)

print(f'Labels saved to {output_path}')
