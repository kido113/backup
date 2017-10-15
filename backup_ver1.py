import os
import time

#文件位置
source = ['F:\\text']

#备份位置
target_dir = 'F:\\Backup'

#zip文件名为日期时间
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#如果目标目录不存在则进行创建
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#zip命令进行打包
zip_command = 'rar a {0} {1}'.format(target,' '.join(source))

print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0:
	print('successful backup to',target)
else:
	print('backup failed')
