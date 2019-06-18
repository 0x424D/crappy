This repository is a collection of practice programs that I write. Most of them will be random standard algorithms.

I'll write them all without referencing any pseudocode, which is why the code will probably be horrible and messy.

`bsearch`: binary search algorithm in C

`SRTToVTT`: quick python script to convert SRT files to VTT files

`msort`: merge sort algorithm in Python 3.x

`cg_mmult`: a code golf (107 character) implementation of matrix multiplication in Python 3.x

`pwned`: Emulates the functionality of Dr. Mike Pound's script shown in the Computerphile video "Have You Been Pwned?" (full video at https://www.youtube.com/watch?v=hhUb5iknVJs, Dr. Pound's script at https://github.com/mikepound/pwned-search/blob/master/pwned.py)

`pastedump`: Generates a random paste key (8 alphanumeric characters), requests the pastebin page relating to that key and then, if the response code is not 404, dumps the raw paste in the directory the program is run from. The file the paste is dumped in is named the timestamp (from time.time()) plus ".txt". This program runs in the background. Requests are made in 5-second intervals to avoid overloading the server and the computer's processor.
