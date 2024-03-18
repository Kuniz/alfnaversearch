"""
Naver Map Search Workflow for Alfred 5
Copyright (c) 2022 Kyeongwon Lee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import os

from workflow import web, Workflow

default_latitude = os.environ.get('latitude')
default_longitude = os.environ.get('longitude')

def get_data(word):
    url = 'https://map.naver.com/v5/api/search/instant-search'
    params = dict(query=word,
                  type="all",
                  coords= f'{default_latitude},{default_longitude}',
                  lang="ko",
                  caller="pcweb"
                  )
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
    r = web.get(url, params, headers=headers)
    r.raise_for_status()
    return r.json()


def main(wf):
    args = wf.args[0]

    wf.add_item(title=f"Search Naver Map for '{args}'",
                autocomplete=args,
                arg=f"https://map.naver.com/v5/search/{args}",
                quicklookurl=f"https://map.naver.com/v5/search/{args}",
                valid=True)

    def wrapper():
        return get_data(args)

    res_json = wf.cached_data(f"navmap_{args}", wrapper, max_age=30)

    if len(res_json["address"]) > 0:
        for ltxt in res_json["address"]:
            address_key = "fullAddress"
            txt = ltxt[address_key]
            address = ltxt["title"]
            type = ltxt["fullAddress"]
            wf.add_item(
                title=f"Search Naver Map for \'{txt}\'",
                subtitle=address,
                autocomplete=txt,
                arg=f"https://map.naver.com/v5/search/{txt}/{type}",
                copytext=txt,
                largetext=txt,
                quicklookurl=f"https://map.naver.com/v5/search/{txt}/{type}",
                valid=True)
    elif len(res_json["place"]) > 0:
        for ltxt in res_json["place"]:
            address_key = "roadAddress"
            txt = ltxt["title"]
            if not ltxt.get(address_key):
                address_key = "jibunAddress"
            address = ltxt[address_key]
            _id = ltxt["id"]
            type = ltxt["type"]
            wf.add_item(
                title=f"Search Naver Map for \'{txt}\'",
                subtitle=address,
                autocomplete=txt,
                arg=f"https://map.naver.com/v5/search/{txt}/{type}/{_id}",
                copytext=txt,
                largetext=txt,
                quicklookurl=f"https://map.naver.com/v5/search/{txt}/{type}/{_id}",
                valid=True)
    elif len(res_json["bus"]) > 0:
        for ltxt in res_json["bus"]:
            type = "bus-route"
            address_key = ltxt["cityName"]
            txt = ltxt["title"]
            address = address_key + "버스 " + txt
            _id = ltxt["id"]
            wf.add_item(
                title=f"Search Naver Map for \'{txt}\'",
                subtitle=address,
                autocomplete=txt,
                arg=f"https://map.naver.com/v5/search/{txt}/{type}/{_id}",
                copytext=txt,
                largetext=txt,
                quicklookurl=f"https://map.naver.com/v5/search/{txt}/{type}/{_id}",
                valid=True)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
