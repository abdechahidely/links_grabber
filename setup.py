import os
cwd = os.getcwd()
with open('%s/.bashrc'%os.path.expanduser('~') , 'a') as file:
	file.write("\nalias seek='python3 %s/seek.py'"%cwd)