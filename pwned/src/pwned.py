# pwned.py
# This script polls the pwnedpasswords API to test whether a given password has been compromised in a data breach

# Usage: py pwned.py <password>

import hashlib, sys, urllib.request

def main():
	password = sys.argv[1]
	hash = hashlib.sha1(bytes(password, "utf-8"))
	digest = hash.hexdigest().upper()
	url = f"https://api.pwnedpasswords.com/range/{digest[:5]}"

	request = urllib.request.Request(url, headers={"User-Agent":"API-Programming-Exercise"})
	page = urllib.request.urlopen(request)

	data = (page.read().decode('utf-8').split())

	for i in data:
		tmp = i.split(":")
		if digest[:5] + tmp[0] == digest:
			print(f"{password} was found")
			print(f"Hash {digest}, {tmp[1]} occurrences")
			break
	else:
		print(f"Password {password} was not found")
			
if __name__ == "__main__":
	main()
