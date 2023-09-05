import requests
import csv
import json
from datetime import datetime

def read_api_token(file_path):
  with open(file_path, 'r') as file:
    return file.read().strip()

def get_api_data(api_token):
  course_id = input("Enter course id: ")
  topic_id = input("Enter topic id: ")
  
  headers = {"Authorization": f"Bearer {api_token}"}
  
  api_endpoint = \
    f"https://canvas.colorado.edu/api/v1/courses/{course_id}/discussion_topics/{topic_id}/view?include[]=all_entries"
  
  response = requests.get(api_endpoint, headers=headers)
  
  return response.json()

def pull_participants(data):
  names = {participant["id"]: participant["display_name"] for participant in data["participants"]}
  return names

def write_to_csv(data):
  current_date = datetime.now().strftime("%Y-%m-%d")
  filename = f"discussions_participants_{current_date}.csv"
  
  with open(filename, 'w', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'display_name'])
    for key, value in data.items():
      writer.writerow([key, value])