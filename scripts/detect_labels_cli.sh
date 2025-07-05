#!/bin/bash
BUCKET=$1
FILE=$2
REGION=$3

aws rekognition detect-labels \
  --image "S3Object={Bucket=$BUCKET,Name=$FILE}" \
  --max-labels 10 \
  --min-confidence 70 \
  --region $REGION > ./output/labels_${FILE%.*}.json
