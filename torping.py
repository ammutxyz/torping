# Hack the planet
import requests, json, sys

sess = requests.session()
sess.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

iptest = json.loads(sess.get('http://httpbin.org/ip').text)
tortest = str(sess.head(sys.argv[1]).status_code)

print(f'TOR IP: {iptest["origin"]} \nOnion domain status code: {tortest}')