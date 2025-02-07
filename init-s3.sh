#!/bin/bash

# Define the bucket name
BUCKET_NAME="turo-vendors-dropbox"

# Check if the bucket exists
if ! awslocal s3 ls "s3://$BUCKET_NAME" 2>&1 | grep -q 'NoSuchBucket'; then
  echo "Bucket $BUCKET_NAME already exists."
else
  # Create the bucket if it does not exist
  echo "Creating bucket $BUCKET_NAME..."
  awslocal s3 mb "s3://$BUCKET_NAME"
fi