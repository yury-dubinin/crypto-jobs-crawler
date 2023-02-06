from datetime import datetime
import json


def writeHistory(current_jobs:dict):
    now = f'{datetime.date(datetime.now())}'
    with open('history.json', 'r') as f:
        data = json.load(f)
    for job in current_jobs:
        it = data.get(job, {})
        it[now] = current_jobs[job]
        data[job] = it
    with open('history.json', 'w') as file:
        json.dump(data, file, indent=4)

with open('current.json') as json_file:
    data = json.load(json_file)
    writeHistory(dict(data))
