from browsers.chromium import Chromium
from browsers.firefox import Firefox

browser_id = 'XXX'  # TODO

print('Starting up Chromium...')
chromium = Chromium(browser_id, 9223)
chromium.navigate('http://127.0.0.1:3000/')
chromium.click(100, 100)
chromium.close_connection()

print('Starting up Firefox...')
firefox = Firefox(port=9222)
firefox.navigate('http://127.0.0.1:3000/')
firefox.click(100, 100)
firefox.close_connection()