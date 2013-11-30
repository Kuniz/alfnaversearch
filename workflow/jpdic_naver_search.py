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
import re;

items = [];
str = '';

if len(alp.args()) > 0:
	str = alp.args()[0];
	iDict = dict(title = ('Search Naver Jpdic for \'' + str + '\''), autocomplete=str, arg=str,valid='true');
	i = alp.Item(**iDict);
	items.append(i);

chk = bool(re.match('[a-zA-Z]+', str));

res = alp.Request('http://jpdic.naver.com/ac?st=111&r_lt=111&n_kojpdic=1&q=' + str);
res.download();

res_json = res.request.json();

for ltxt in res_json['items'][0]:
	if len(ltxt) > 0:
		txt = ltxt[0][0];
		rtxt = ltxt[1][0];
		argtxt = txt;
		if chk:
			argtxt = rtxt;

		iDict = dict(title = (txt + ' \t\t ' + rtxt) ,subtitle = ('Search Naver Jpdic for \'' + txt + '\''), autocomplete=txt, arg=argtxt,valid='true');
		i = alp.Item(**iDict);
		items.append(i);

alp.feedback(items);
