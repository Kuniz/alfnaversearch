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




import sys

from workflow import web, Workflow


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
	import cgi;

	args = wf.args[0]

	wf.add_item(title = 'Search Naver Endic for \'%s\'' % args, 
				autocomplete=args, 
				arg=args,
				valid=True)

	def wrapper():
		return get_data(args)


	res_json = wf.cached_data('nav_%s' % args, wrapper , max_age=30)

	for ltxt in res_json['items'][0]:
		if len(ltxt) > 0  :
			txt = ltxt[0];
			wf.add_item(
				title = 'Search Naver for \'%s\'' % txt, 
				autocomplete=txt, 
				arg=txt,
				valid=True);
			
	wf.send_feedback()

				


if __name__ == '__main__':
	wf = Workflow()
	sys.exit(wf.run(main))

