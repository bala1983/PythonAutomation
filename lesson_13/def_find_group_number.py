import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_group_numbers(search_number) -> str:

    tree = ET.parse('groups.xml')
    groups = tree.getroot()

    for group in groups:
        number = group.find('number')
        number_text = int(number.text)
        if int(search_number) == number_text:
            timing_exbytes = group.find('timingExbytes')
            incoming = timing_exbytes.find('incoming')
            results = incoming.text
            logging.info(results)

input_number = input("input number of group you want to search: ")

find_group_numbers(input_number)