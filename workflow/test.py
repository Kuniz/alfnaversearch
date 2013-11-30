#  Naver Search Workflow for Alfred 2
#  Copyright (C) 2013  Jinuk Baek
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


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