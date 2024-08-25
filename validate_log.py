import re

def validate_log(file_path: str) -> str:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if len(lines) < 2 or lines[0].strip() != '.LOG':
            return 'Invalid file content. The file must start with .LOG.'
        
        # Check the second line for the time and date format
        time_date_pattern = r'^\d{2}:\d{2} \d{2}-\d{2}-\d{4}$'
        if not re.match(time_date_pattern, lines[1].strip()):
            return 'Invalid file content. The second line must be in the format HH:MM DD-MM-YYYY.'
        return 'File successfully uploaded and is a .txt file.'