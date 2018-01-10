#! /usr/bin/python

import threading
import datetime


password = 'pass'
filename = str('backup-{0}_{1}.zip'.format(datetime.datetime.now().date(),datetime.datetime.now().time())).replace(':','-')
username = 'username'
ip = 'ip'
dest_dir = 'Destination_Of_Backup eg: /home/username/folder'
script_name = 'backup.sh'
 
# create and Transfer Backup
def backup(filename,password,username,ip,dest_dir,script_name):
    with open(script_name, 'w') as backup:
        backup.write('#! bin/bash\nzip -r {0} data\nsshpass -p {1} scp {2} {3}@{4}:{5}\nrm -rf {6}\n'.format(filename,password,filename,username,ip,dest_dir,filename))
    run_backup(script_name)

def run_backup(script_name):
    import os
    os.system('sh {0} >> /dev/null'.format(script_name))
    os.system('rm -rf {0}'.format(script_name))
if __name__ == '__main__':
    backup = threading.Thread(target=backup, args=(filename,password,username,ip,dest_dir,script_name))
    backup.start()
    del password, filename, username, ip, dest_dir, script_name