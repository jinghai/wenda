import requests
from bottle import route, response, request, static_file, hook
import re
from plugins.common import settings,allowCROS
def find(search_query,step = 0):
    return []

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'}
proxies = {"http": None,"https": None,}


@route('/api/sd_agent', method=("POST","OPTIONS"))
def api_find():
    allowCROS()
    url = "http://127.0.0.1:786"
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=request.json, proxies=proxies)
    r = response.text
    return r

@route('/assets/<path:path>')#wenda-webui
def webui(path='-'):
    if path.endswith(".js"):
        return static_file(path, root="views/static/wenda-webui/assets", mimetype="application/javascript")
    return static_file(path, root="views/static/wenda-webui/assets")