from browsers.chromium import Chromium

browser_id = 'XXX'  # TODO

print('Starting up Chromium...')
chromium = Chromium(browser_id, 100, 9223)
chromium.navigate('http://127.0.0.1:3000/')
chromium.click(100, 100)