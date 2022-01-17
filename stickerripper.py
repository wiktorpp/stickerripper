import requests

x=open("file.har", "r").read()
null=None
exec("a="+x)
urls=[]
for entry in a["log"]["entries"]:
	urls.append(entry["request"]["url"].split("?")[0] + "?size=640")

for url in urls:
	open(
		url.split("/")[-1].split("?size=640")[0], 'wb'
	).write(
		requests.get(url, allow_redirects=True).content
	)
