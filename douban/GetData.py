from urllib import request
resp = request.urlopen('https://movie.douban.com/cinema/nowplaying/guangzhou/')
html_data = resp.read().decode('utf-8')
print(html_data)