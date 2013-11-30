"""
Naver Search Workflow for Alfred 2
Copyright (C) 2013  Jinuk Baek
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


import alp;
import json;

items = [];
str = '';

if len(alp.args()) > 0:
	str = alp.args()[0];
	iDict = dict(title = ('Search Naver for \'' + str + '\''), autocomplete=str, arg=str,valid='true');
	i = alp.Item(**iDict);
	items.append(i);

res = alp.Request('http://ac.search.naver.com/nx/ac?&q_enc=UTF-8&st=100&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&ans=1&run=2&rev=4&q=' + str);
res.download();

res_json = res.request.json();

for ltxt in res_json['items'][0]:
	if len(ltxt) > 0  :
		txt = ltxt[0];
		iDict = dict(title = ('Search Naver for \'' + txt + '\''), autocomplete=txt, arg=txt,valid='true');
		i = alp.Item(**iDict);
		items.append(i);

alp.feedback(items);
