from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

session = HTMLSession()
asession = AsyncHTMLSession()

#r = session.get('https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship', verify=False)
#r = session.get('https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship')

#async def get_jw():
#  s = await asession.get('https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship')

s = await asession.get('https://www.jw.org/en/library/videos/#en/categories/VODPgmEvtMorningWorship')
#r = session.get('http://python-requests.org')

#r.html.render()
#print(r.text)

#result = session.run(get_jw)
print(result)
s.html.render()
print(s.text)
