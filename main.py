from discussions import pull

def main():
  
  with open('course_id.txt', 'r') as file:
    line = file.readline().strip()
    
  course_numbers = [x.strip() for x in line.split(',')]
  
  filepath = 'token.txt'
  api_token = pull.read_api_token(filepath)
  
  data = pull.get_api_data(api_token)
  
  participants = pull.pull_participants(data)
  
  pull.write_to_csv(participants)
  
  
  print(course_numbers)
  
if __name__ == "__main__":
  main()