import os
import io
import csv
import json
import time
import boto3
import requests
from datetime import datetime

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')
dynamo_client = boto3.resource('dynamodb')

# For each HSK level: Get a random word, fill in email template, create and send a campaign, send error notification on failure
def lambda_handler(event, context):

  print("Testing requests", requests.get("https://google.com"))

