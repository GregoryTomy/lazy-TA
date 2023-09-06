import requests
import csv
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

API_ENDPOINT_TEMPLATE = "https://canvas.colorado.edu/api/v1/courses/{course_id}/discussion_topics/{topic_id}/view?include[]=all_entries"

class CourseTopicInfo():
  """Holds course and topic IDs"""
  def __init__(self, course_id, topic_id):
    self.course_id = course_id
    self.topic_id = topic_id
    
def read_api_token(file_path):
  """Read API token from file"""
  try:
    with open(file_path, 'r') as file:
      return file.read().strip()
  except Exception as e:
    logging.error(f"Failed to read API token: {e}")
    return None

def get_course_topic_info():
  """Get course and topic id from user"""
  course_id = input("Enter course id: ")
  topic_id = input("Enter topic id: ")
  
  return CourseTopicInfo(course_id, topic_id)

def get_api_data(api_token, course_topic_info):
  """Fetch data from API"""
  headers = {"Authorization": f"Bearer {api_token}"}
  api_endpoint = \
    API_ENDPOINT_TEMPLATE.format(
      course_id=course_topic_info.course_id,
      topic_id=course_topic_info.topic_id
      ) 
  try:
    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
  except requests.RequestException as e:
    logging.error(f"API request failed: {e}")
    return None

def pull_participants(data):
  """Extract participant names from API data"""
  names = {participant["id"]: participant["display_name"] for participant in data["participants"]}
  return names

def write_to_csv(data, course_topic_info):
  """Write participant information to CSV file"""
  current_date = datetime.now().strftime("%Y-%m-%d")
  filename = \
    f"disc_part_{course_topic_info.course_id}_{course_topic_info.topic_id}_{current_date}.csv"
  
  try:
    with open(filename, 'w', newline= '') as f:
      writer = csv.writer(f)
      writer.writerow(['id', 'display_name'])
      for key, value in data.items():
        writer.writerow([key, value])
  except Exception as e:
    logging.error(f"Failed to write to CSV: {e}")