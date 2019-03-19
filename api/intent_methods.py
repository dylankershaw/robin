import datetime


class IntentMethods:
    def greeting():
        return 'Well hello there.'

    def get_time():
        time = datetime.datetime.now()

        hour = time.hour % 12
        if hour == 0:
            hour = 12

        if time.minute == 0:
            minutes = 'o clock'
        elif time.minute < 10:
            minutes = 'o ' + str(time.minute)
        else:
            minutes = time.minute

        return f'The time is {hour} {minutes}'

    def intent_not_found():
        return 'I don\'t understand'
