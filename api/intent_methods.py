from datetime import datetime
from pytz import timezone
import requests
import os


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

    def get_weather(latitude=40.7128, longitude=-74.0060):
        r = requests.get(
            f"https://api.darksky.net/forecast/{os.environ.get('DARKSKY_KEY')}/{latitude},{longitude}"
        ).json()

        temp = round(r['currently']['temperature'])
        feels_like = round(r['currently']['apparentTemperature'])
        summary = r['hourly']['summary']

        return f'It is currently {temp} degrees but feels like {feels_like}. {summary}'

    def intent_not_found():
        return 'I don\'t understand, but I\'m learning every day.'
