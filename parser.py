import pprint
import csv
import re
from datetime import datetime, date, time
from getters.station import get_station_from_text
from getters.time import get_time_from_text, get_text_without_time
from getters.state import get_state_from_text

pp = pprint.PrettyPrinter(indent=4)

OPEN_REGEXP = r'[Вв ]*([\d]{2})-([\d+]{2}) (вестибюль [1-2] ст.|ст.) ([а-яёй А-Я-12]+) открыт[аы]*[,.]{1} ([а-яёй А-Я]+)'
CLOSED_REGEXP = r'[Вв ]*([\d]{2})-([\d+]{2}) (вестибюль [1-2] ст.|ст.) ([а-яёй А-Я-12]+) закрыт[аы]+[на вход.]* ([а-яёй А-Я-]+)'

data = []

with open(file='./imported_data.csv', mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        event = dict()
        raw_message = row['Raw Message']
        event['raw_message'] = raw_message
        event['message_length'] = len(raw_message)
        event['message_timestamp'] = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
        event['date'] = date(int(row['Date'][0:4]), int(row['Date'][5:7]), int(row['Date'][8:10]))
        event['view_count'] = row['View Count']
        open_result = re.match(OPEN_REGEXP, raw_message)
        closed_result = re.match(CLOSED_REGEXP, raw_message)
        
        if open_result is not None:
            results = open_result.groups()
            event['time'] = time(int(results[0]), int(results[1]))
            event['datetime'] = datetime.combine(event['date'], event['time'])
            event['station'] = results[3]
            event['reason'] = results[4]
            event['state'] = 'open'

        elif closed_result is not None:
            results = closed_result.groups()
            event['time'] = time(int(results[0]), int(results[1]))
            event['datetime'] = datetime.combine(event['date'], event['time'])
            event['station'] = results[3]
            event['reason'] = results[4]
            event['state'] = 'closed'

        else:
            event['time'] = get_time_from_text(raw_message)
            if event['time'] is not None:
                event['datetime'] = datetime.combine(event['date'], event['time'])
            else:
                event['datetime'] = None
            event['station'] = get_station_from_text(get_text_without_time(raw_message))
            event['state'] = get_state_from_text(raw_message)
            event['reason'] = None
        
        data.append(event)


with open(file='./parsed_data.csv', mode='a',) as output_file:
    dict_writer = csv.DictWriter(output_file, data[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(data)

pp.pprint(data)
print('{} of {} is done'.format(len([x for x in data if x['reason'] is not None]), len(data)))
