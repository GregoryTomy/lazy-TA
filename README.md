# Canvas Discussion Participants Extractor

## Overview

This program allows you to extract the names of students who have participated in a specific discussion topic for a course on Canvas. The program accesses the Canvas API, fetches relevant data, and saves the participant names and IDs into a CSV file.

## Requirements

- Python 3.x
- `requests` library
- `csv` library
- `json` library
- `datetime` library

## Installation

1. Clone the repository or download the ZIP file.
2. Install the required Python libraries:

    ```bash
    pip install requests
    ```

## Configuration

### API Token

You need to generate an API token from your Canvas account.

1. Go to Canvas Account > Settings > Approved Integrations or Developer Keys (depending on your Canvas setup).
2. Create a new API Token.
3. Save this token in a text file named `token.txt` in the same directory as the program.

You can read more about how to generate API tokens from the [Canvas API documentation](https://canvas.instructure.com/doc/api/file.oauth.html).

### Course and Topic IDs

1. Navigate to the discussion topic on Canvas you are interested in.
2. The URL should look like `https://canvas.colorado.edu/courses/{course_id}/discussion_topics/{topic_id}`.
3. Note down the `course_id` and `topic_id`.

> **Note**: If you are using Canvas from a different university, you will need to update the domain name in the `pull.py` file. For example, change `https://canvas.colorado.edu` to your university's Canvas URL.

## Usage

1. Run `main.py`:

    ```bash
    python main.py
    ```

2. When prompted, enter the `course_id` and `topic_id`.

3. The program will output a CSV file named `discussion_participants_{current_date}.csv`. For example, if run on September 5, 2023, the file will be named `discussions_participants_2023-09-05`.

## Code Structure

- `pull.py`: Contains functions to read the API token, make API calls, extract participant data, and write data to a CSV file.
- `main.py`: The entry point of the application. It reads course IDs from `course_id.txt`, calls functions from `pull.py`, and handles data flow.

## License

This project is open-source and available under the MIT License. See `LICENSE` file for details.

---

For any issues, please create an issue on the GitHub repository.
