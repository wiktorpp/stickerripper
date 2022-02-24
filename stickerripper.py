import requests

null=None
exec("data="+open("file.har", "r").read())
urls=[]
for entry in data["log"]["entries"]:
    urls.append(entry["request"]["url"].split("?")[0] + "?size=640")

for url in urls:
    open(
        url.split("/")[-1].split("?size")[0], 'wb'
    ).write(
        requests.get(url, allow_redirects=True).content
    )
