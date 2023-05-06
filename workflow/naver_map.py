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

from workflow import web, Workflow

def get_data(word):
    url = 'https://map.naver.com/v5/api/search'
    params = dict(query=word,
                  type="all",
                  displayCount="10",
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
    res_type = res_json["result"]["type"] # address, place, bus

    if res_type == "address":
        if res_json["result"][res_type]["subType"] == "jibun-address":
            res_list = res_json["result"][res_type]["jibunsAddress"]["list"]
        else:
            res_list = res_json["result"][res_type]["roadAddress"]["list"]
        address_key = "koreanAddress"
        for ltxt in res_list:
            if len(ltxt) > 0:
                txt = ltxt[address_key].strip()
                address = ltxt["name"]
                wf.add_item(
                    title=f"Search Naver Map for \'{txt}\'",
                    subtitle=address,
                    autocomplete=txt,
                    arg=f"https://map.naver.com/v5/search/{txt}/{res_type}",
                    copytext=txt,
                    largetext=txt,
                    quicklookurl=f"https://map.naver.com/v5/search/{txt}/{res_type}",
                    valid=True)
    elif res_type == "place":
        res_list = res_json["result"][res_type]["list"]
        address_key = "roadAddress"
        for ltxt in res_list:
            if len(ltxt) > 0:
                txt = ltxt["name"]
                address = ltxt[address_key]
                _id = ltxt["id"]
                wf.add_item(
                    title=f"Search Naver Map for \'{txt}\'",
                    subtitle=address,
                    autocomplete=txt,
                    arg=f"https://map.naver.com/v5/search/{txt}/{res_type}/{_id}",
                    copytext=txt,
                    largetext=txt,
                    quicklookurl=f"https://map.naver.com/v5/search/{txt}/{res_type}/{_id}",
                    valid=True)
    elif res_type == "bus":
        res_list = res_json["result"][res_type]["busRoute"]["list"]
        res_type = "bus-route"
        address_key = "cityName"
        for ltxt in res_list:
            if len(ltxt) > 0:
                txt = ltxt["name"]
                address = ltxt[address_key] + "버스 " + txt
                _id = ltxt["id"]
                wf.add_item(
                    title=f"Search Naver Map for \'{txt}\'",
                    subtitle=address,
                    autocomplete=txt,
                    arg=f"https://map.naver.com/v5/search/{txt}/{res_type}/{_id}",
                    copytext=txt,
                    largetext=txt,
                    quicklookurl=f"https://map.naver.com/v5/search/{txt}/{res_type}/{_id}",
                    valid=True)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
