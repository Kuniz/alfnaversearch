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

import sys;
import alfred;
import json;
import urllib2;

pct_query = urllib2.quote(sys.argv[1]);

sys.stderr.write(pct_query + '\n' );
sys.stderr.write(sys.argv[1]);

response = urllib2.urlopen('http://ac.search.naver.com/nx/ac?q='+
pct_query
+ '&q_enc=UTF-8&st=100&frm=nv&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=1&run=2&rev=4');
html = response.read();
response.close();

res_json = json.loads(html);

feedback = alfred.Feedback();

for ltxt in res_json['items'][0]:
	if len(ltxt) > 0  :
		txt = ltxt[0];
		feedback.addItem(title = ('Search for Naver ' + txt), autocomplete=txt, arg=txt,valid='yes');

feedback.output();
