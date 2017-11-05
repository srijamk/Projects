import os
path = os.path.join('Users', 'Kiran', 'BitTorrent Sync', 'Srija_Work')
cwd = os.getcwd()
print "Path: " + path
print "Cwd: " + cwd
os.chdir('/Users/Kiran')
print "New Cwd: " + os.getcwd()
print "Abspath: " + os.path.abspath('.')
print "New Abspath: " + os.path.abspath('.\\BitTorrent Sync')
print "Is path abs? " + os.path.isabs('.')