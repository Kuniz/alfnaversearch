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


import sys

from workflow import web, Workflow


def get_dictionary_data(word):
	url = 'https://ac.dict.naver.com/hanja/ac'
	params = dict(q_enc='utf-8',
		st=111,
		r_format='json',
		r_enc='utf-8',
		q=word)


	r = web.get(url, params)
	r.raise_for_status()
	return r.json()


def main(wf):
	import cgi;

	args = wf.args[0]

	wf.add_item(title = 'Search Naver Hanja for \'%s\'' % args, 
				autocomplete=args, 
				arg=args,
				valid=True)

	def wrapper():
		return get_dictionary_data(args)

	res_json = wf.cached_data("hanja_%s" % args, wrapper, max_age=600)

	for item in res_json['items']:
		for ltxt in item:
			if len(ltxt) > 0:
				txt = ltxt[0][0];
				rtxt = cgi.escape(ltxt[1][0]);

				wf.add_item(title = u"%s     %s" % (txt, rtxt) ,
							subtitle = 'Search Naver Hanja for \'%s\'' % txt, 
							autocomplete=txt, 
							arg=txt,
							valid=True);

	wf.send_feedback()
				


if __name__ == '__main__':
	wf = Workflow()
	sys.exit(wf.run(main))


