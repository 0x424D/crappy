import hashlib, sys, urllib.request

def main():
	hash = hashlib.sha1(bytes(sys.argv[1], "utf-8"))
	digest = hash.hexdigest().upper()
	url = f"https://api.pwnedpasswords.com/range/{digest[:5]}"

	request = urllib.request.Request(url, headers={"User-Agent":"API-Programming-Exercise"})
	page = urllib.request.urlopen(request)

	data = (page.read().decode('utf-8').split())

	for i in data:
		tmp = i.split(":")
		if digest[:5] + tmp[0] == digest:
			print(f"{sys.argv[1]} was found")
			print(f"Hash {digest}, {tmp[1]} occurrences")
			
if __name__ == "__main__":
	main()
