from datetime import datetime
import pytz


def current_time_stamp():
    return int(datetime.now(pytz.timezone('Asia/Saigon')).timestamp())
