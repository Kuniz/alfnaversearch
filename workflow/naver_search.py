"""
Naver Search Workflow for Alfred 2
Copyright (c) 2021 Jinuk Baek

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

if sys.version[0] == "2":
    from workflow import web, Workflow
else:
    from workflow3 import web, Workflow


def get_data(word):
    url = 'http://ac.search.naver.com/nx/ac'

    params = dict(q_enc='UTF-8',
                  st=100,
                  r_format='json',
                  r_enc='UTF-8',
                  r_unicode=0,
                  t_koreng=1,
                  ans=1,
                  run=2,
                  rev=4,
                  q=word
                  )

    r = web.get(url, params)
    r.raise_for_status()
    return r.json()


def main(wf):
    args = wf.args[0]

    wf.add_item(title='Search Naver for \'%s\'' % args,
                autocomplete=args,
                arg=args,
                valid=True)

    def wrapper():
        return get_data(args)

    res_json = wf.cached_data('nav_%s' % args, wrapper, max_age=30)

    for ltxt in res_json['items'][0]:
        if len(ltxt) > 0:
            txt = ltxt[0]
            wf.add_item(
                title='Search Naver for \'%s\'' % txt,
                autocomplete=txt,
                arg=txt,
                valid=True)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
