#coding=utf-8
import os, sys 
import csv
import subprocess
import StringIO

'''
please execute the script under pydio/core/src 
'''


ROOT_USER='admin'
ROOT_PWD='cmcc1234'
PYDIO_ROOT='/Users/cmcc/experiment/pydio-core/core/src'
ADD_USER_SCRIPT = 'php cmd.php -u={} -p={} -r=ajxp_conf -a=create_user --new_user_login={} --new_user_pwd={}'
MKDIR_CMD = 'mkdir -p data/personal/{}'
CHMOD_CMD = 'chown -R nodody:nobody data\n chmod -R 777 data'
COMMON_FILES_ROOT_DIR = '{}/data/files'
LINK_DIR = 'cd data/personal/{}\n ln -s ../../files/{}\n cd ../../ '


def setup_env_eachuser(username, pwd):
    output = StringIO.StringIO()
    # create new user

    print ADD_USER_SCRIPT.format(ROOT_USER, ROOT_PWD, username, pwd)
    subprocess.call(ADD_USER_SCRIPT.format(ROOT_USER, ROOT_PWD, username, pwd), shell=True)
    subprocess.call(MKDIR_CMD.format(username), shell=True)
    # link dirs
    output.close()
    for dirname in os.listdir('data/files'):
        print LINK_DIR.format(username, dirname, username)
        subprocess.call(LINK_DIR.format(username, dirname, username), shell=True)


def parse_agents(filename):
    with open(filename, 'rb') as csvfile:
        agentreader = csv.reader(csvfile, delimiter=',')
        for row in agentreader:
            username = row[2]
            pwd = row[1]
            setup_env_eachuser(username, pwd)
    subprocess.call(CHMOD_CMD, shell=True)
           
if __name__ == '__main__' :
    if len(sys.argv) < 2:
        print 'Usage: python add_user.py agent_file_name'
    parse_agents(sys.argv[1])
        
