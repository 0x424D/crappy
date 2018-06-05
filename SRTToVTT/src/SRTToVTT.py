import os.path, sys, fileinput
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*#
#~*~*~*~*~*~*~*~* Exit values ~*~*~*~*~*~*~*~*~*~*~#
#            0: everything is fine                 #
#        1: file to convert does not exist         #
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*#
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*#
 
def replaceStr(filePath, pattern, subst):
    fh, absPath = mkstemp()
    with fdopen(fh,'w') as newFile:
        with open(filePath) as oldFile:
            for line in oldFile:
                newFile.write(line.replace(pattern, subst))
    
    remove(filePath)
    move(absPath, filePath)
 
def main():
	print("Enter the name of the file to convert")
	fileName = input("> ")
	
	if not os.path.isfile(fileName):
		print("Error: file not found.")
		sys.exit(1)
	
	with open(fileName, "r") as f:
		data = f.read()
	
	with open(fileName.replace(".srt", ".vtt"), "w+") as g:
		g.write("WEBVTT FILE\n\n" + data)
		
		g.seek(0)
		
		data = g.read()
	
	for i in range(10):
		replaceStr(fileName.replace(".srt", ".vtt"), "," + str(i), "." + str(i))
		
	remove(fileName)

if __name__ == "__main__":
	main()
