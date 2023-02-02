from datetime import datetime

def seconds_to_date(v):
    if isinstance(v, str) or not v:
        return ''
    d = datetime.fromtimestamp(v).strftime('%Y-%m-%dT%H:%M:%S')
    return d

def timestamp():
    return datetime.now().strftime('%y_%m_%d_%H_%M_%S')