import os
import time

source = ['F:\\text']

target_dir = 'F:\\Backup'


if not os.path.exists(target_dir):
	os.mkdir(target_dir)


today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

#添加用户的注释
comment = input('Enter a comment-->')

if len(comment) ==0:
	target = today + os.sep + now +'.zip'
else:
	target = today + os.sep + now +'_'+comment.replace(' ','_') + '.zip'

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