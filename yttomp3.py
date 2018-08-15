import sys
import time
import os
import pafy
import pip



def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def checkexistance(fname):
	if (os.path.isfile(fname)==False):
	    return False
	else:
	    return True
def download(contents):
	for i in contents:
		url = i[0]
		new_name = ""
		for j in i[1:]:
			new_name = new_name+" "+j
		new_name = new_name[1:]
		audio = pafy.new(url)
		title = audio.title
		#get best resolution regardless of format
		best = audio.getbestaudio()
 
		print(best.resolution, best.extension)
		best.download()
		os.rename(title+".webm",new_name)

def main():
	install_and_import('pygame')
	install_and_import('pafy')
	fname = sys.argv[1]
	if not checkexistance(fname):
		print("This file does not exist.Exiting......")
		time.sleep(2)
		sys.exit(1)
	else:
		fd = open(fname,"r")
		contents = fd.read()
		contents = list(contents.splitlines())
		for i in range(len(contents)):
			contents[i] = list(contents[i].split(" "))
		download(contents)
		#print(contents)
		#contents ready
		


if __name__== "__main__":
	main()
