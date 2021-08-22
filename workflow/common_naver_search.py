# Naver Search Workflow for Alfred 2
# Copyright (c) 2021 Jinuk Baek
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys

from workflow import web, Workflow


def get_dictionary_data(lang, word):
    url = 'https://ac-dict.naver.com/%sko/ac' % lang
    params = dict(q=word,
                  _callback='',
                  q_enc='UTF-8',
                  st=11,
                  r_lt='10',
                  r_format='json',
                  r_enc='UTF-8')

    r = web.get(url, params)
    r.raise_for_status()
    return r.json()


def main(wf):
    import cgi;

    lang = wf.args[0]
    word = wf.args[1]

    wf.add_item(title = 'Search Naver %sdic for \'%s\'' % (lang, word),
                autocomplete=word,
                arg=word,
                valid=True)

    def wrapper():
        return get_dictionary_data(lang, word)

    res_json = wf.cached_data("%s_%s" % (lang, word), wrapper, max_age=600)

    for item in res_json['items']:
        for ltxt in item:
            if len(ltxt) > 0:
                txt = ltxt[0][0]
                rtxt = cgi.escape(ltxt[3][0])

                wf.add_item(title = u"%s     %s" % (txt, rtxt) ,
                            subtitle = 'Search Naver %sdic for \'%s\'' % (lang, txt),
                            autocomplete=txt,
                            arg=txt,
                            valid=True)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
