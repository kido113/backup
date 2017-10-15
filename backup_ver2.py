import os
import time

source = ['F:\\text']

target_dir = 'F:\\Backup'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today +os.sep + now +'.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('successfully created directory',today)

zip_command = 'rar a {0} {1}'.format(target,' '.join(source))

print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
	print('successful backup to',target)
else:
	print('backup failed')