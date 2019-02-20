This repository is a collection of practice programs that I write. Most of them will be random standard algorithms.

I'll write them all without referencing any pseudocode, which is why the code will probably be horrible and messy.

`bsearch`: binary search algorithm in C

`SRTToVTT`: quick python script to convert SRT files to VTT files

`scuffedsort`: this was supposed to be a merge sort, but it turned out differently. No pseudocode was referenced so it's weird. Accepts a list with at most 997 elements before reaching maximum recursion depth with default Python 3.6.2 (the maximum recursion depth can be increased with a `sys.setrecursionlimit(n)` call, but the default, slightly conservative estimate exists to prevent stack overflow. It would be dangerous to significantly increase it)

`msort`: merge sort algorithm in Python 3.x. Max list length 997 by default.
