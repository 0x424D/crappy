import requests, random, time

random.seed()

allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while True:
	rand = ""
	for i in range(8):
		rand += random.choice(allowedChars)
	r = requests.get(f"https://www.pastebin.com/{rand}")
	
	print(rand)
	if r.status_code != 404:
		print(r.status_code)
		with open(f"{rand}.txt", "w") as f:
			r = requests.get(f"https://www.pastebin.com/raw/{rand}")
			f.write(r.text)
	else:
		print("404")
	time.sleep(5)
