import json
import logging
import os

logging.basicConfig(
    filename='json_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

folder_path = r'C:\Users\Oleksandr\PycharmProjects\PythonAutomation\PythonAutomation\lesson_13'

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        full_path = os.path.join(folder_path, filename)
        try:
            with open(full_path, 'r', newline='', encoding='utf-8') as jsonfile:
                json.load(jsonfile)
        except json.JSONDecodeError as e:
            logging.error(f'Error in file {filename}: {e}')

    print(f'Check: {filename}')