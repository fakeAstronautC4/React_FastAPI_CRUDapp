import requests





url = "https://wordsapiv1.p.rapidapi.com/words/hatchback/typeOf"

headers = {
	"X-RapidAPI-Key": "f387a74988mshc044007442aeb03p146f67jsn5ec96686aabb",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)


if response.status_code == 200:



print(response.text)