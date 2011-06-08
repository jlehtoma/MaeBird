import os

from fabric.api import env, put, run
from fabric.contrib.project import rsync_project

env.user = 'root'
env.hosts = ['192.168.2.15']

TARGET_WORKSPACE = '/home/user/CodeVault/'
TARGET_PROJECT = 'maebird'
TARGET_MAIN_FILE = 'maebird/main.py'
TARGET = os.path.join(TARGET_WORKSPACE, TARGET_PROJECT, TARGET_MAIN_FILE)

def sync_n_run():
    sync(TARGET_WORKSPACE)
    run_remote(TARGET)
    
def sync(path):
    rsync_project(path)
    
def run_remote(target, cmd='python'):
    run('%s %s' % (cmd, target))