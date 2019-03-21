from datetime import datetime
from pytz import timezone


class IntentMethods:
    def greeting():
        return 'Well hello there.'

    def get_time():
        tz = timezone('US/Eastern')
        time = datetime.now(tz)

        hour = time.hour % 12
        if hour == 0:
            hour = 12

        if time.minute == 0:
            minutes = 00
        elif time.minute < 10:
            minutes = '0' + str(time.minute)
        else:
            minutes = time.minute

        return f'The time is {hour}:{minutes}'

    def intent_not_found():
        return 'I don\'t understand'
