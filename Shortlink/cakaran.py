import requests

def shorten_link(full_link):
    API_KEY = '28299270c38eb346d372112bdbaefed14bc4a'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short' : full_link, 'name' : None}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print(' ')

    try:
      title = data['url']['title']
      short_link = data['url']['shortLink']

      print('Title:', title)
      print('Link:', short_link)
    except:
      status = data['url']['status']
      print('Error Status :', status)

link = input('Enter a link --->>> ')

shorten_link(link)