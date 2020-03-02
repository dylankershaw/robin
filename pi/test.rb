require 'httparty'
require 'tts'

response = HTTParty.get('http://api-robin.herokuapp.com/query/?phrase=yo')
response['response'].play