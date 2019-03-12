import datetime


class IntentMethods:
    def greeting():
        return 'Well hello there.'

    def get_time():
        time = datetime.datetime.now()
        minutes = "o clock" if time.minute == 0 else time.minute
        return f'The time is {time.hour} {minutes}'
