import csv
import re
from datetime import datetime
OPEN_REGEXP = r'В ([\d]{2})-([\d+]{2}) (вестибюль [1-2] ст.|ст.) ([а-я А-Я-12]+) открыт[аы]*[,.]{1} ([а-я А-Я]+)'
CLOSED_REGEXP = r'В ([\d]{2})-([\d+]{2}) (вестибюль [1-2] ст.|ст.) ([а-я А-Я-12]+) закрыт[аы]* (из-за [а-я А-Я]+)'

data = []
event = dict()

with open(file='./imported_data.csv', mode='r', encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        event['raw_message'] = row['Raw Message']
        event['message_timestamp'] = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
        # need only date?
        #event['date'] = 
        event['view_count'] = row['View Count']
        open_result = re.match(OPEN_REGEXP, row['Raw Message'])
        closed_result = re.match(CLOSED_REGEXP, row['Raw Message'])
        if open_result is not None:
            results = open_result.groups()
            event['time'] = datetime(hour=results[0], minute=results[1])
            event['station'] = results[3]
            event['reason'] = results[4]
            event['state'] = 'open'
        elif closed_result is not None:
            results = closed_result.groups()
            event['time'] = datetime(hour=results[0], minute=results[1])
            event['station'] = results[3]
            event['reason'] = results[4]
            event['state'] = 'closed'
        else:
            event['state'] = 'unknown'

        data.append(event)
        
print(data)
