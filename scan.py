import os

p=os.popen('/usr/bin/zbarcam /dev/video1', 'r')
while True:
    code = p.readline()
    print 'Got barcode:', code
    isbn = code.split(':')[1]
    os.system('google-chrome http://www.goodreads.com/search/search?q=%s'%isbn)
