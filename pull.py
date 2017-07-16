# %%
import requests

response = requests.get("https://api.newsriver.io/v2/search?query=language%3AEN%20OR%20text%3Aethereum&sortBy=_score&sortOrder=DESC", headers={"Authorization":"sBBqsGXiYgF0Db5OV5tAwzzfEVTj2i3frBYzgL2ELCDP1HhywHCamL5RUqFTkUF9"})

# %%
jsonFile = response.json()
print(x['publishDate' ] for x in jsonFile)
print(len(jsonFile))
