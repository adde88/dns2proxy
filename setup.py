import sys, os, shutil
from distutils.core import setup, Extension


shutil.copyfile("dns2proxy.py", "dns2proxy/dns2proxy")

setup  (name        = 'dns2proxy',
        version     = '1.0',
        description = 'Offensive DNS server.',
        author = 'Moxie Marlinspike | Andreas Nilsen',
        author_email = 'moxie@thoughtcrime.org | adde88@gmail.com',
        url = 'http://www.github.com/adde88/dns2proxy',
        license = 'GPL',
        packages  = ["dns2proxy"],
        package_dir = {'dns2proxy' : 'dns2proxy/'},
        scripts = ['dns2proxy/dns2proxy'],
        data_files = [('share/dns2proxy', ['README.md'])],
       )

print "Cleaning up..."
try:
    removeall("build/")
    os.rmdir("build/")
except:
    pass

try:
    os.remove("dns2proxy/dns2proxy")
except:
    pass

def capture(cmd):
    return os.popen(cmd).read().strip()

def removeall(path):
	if not os.path.isdir(path):
		return

	files=os.listdir(path)

	for x in files:
		fullpath=os.path.join(path, x)
		if os.path.isfile(fullpath):
			f=os.remove
			rmgeneric(fullpath, f)
		elif os.path.isdir(fullpath):
			removeall(fullpath)
			f=os.rmdir
			rmgeneric(fullpath, f)

def rmgeneric(path, __func__):
	try:
		__func__(path)
	except OSError, (errno, strerror):
		pass
