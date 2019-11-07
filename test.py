import requests

res = requests.get('https://api.github.com/events')
print('** status_code = {} **'.format(res.status_code))
