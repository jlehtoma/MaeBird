from __future__ import with_statement
import os
from fabric.api import env, put, run, cd
from fabric.contrib.project import rsync_project, upload_project

env.user = 'user'
env.hosts = ['192.168.2.15']

TARGET_WORKSPACE = '/home/user/CodeVault/'
TARGET_PROJECT = os.path.join(TARGET_WORKSPACE, 'maebird')
TARGET_MAIN_FILE = 'main.py'
TARGET = os.path.join(TARGET_WORKSPACE, TARGET_PROJECT, TARGET_MAIN_FILE)

EXCLUDES = ['*.pyc', '*.pyo']

def deploy_n_run(remote='sync'):
    if remote == 'sync':
        sync()
    elif remote == 'upload':
        upload()
    run_remote(TARGET_PROJECT, TARGET_MAIN_FILE)
    
def sync(remotedir=TARGET_WORKSPACE, localdir=None):
    rsync_project(remotedir, localdir, exclude=EXCLUDES)
    
def run_remote(project, mainfile, cmd='python'):
    with cd(project):
        run('%s %s' % (cmd, mainfile))
    
def upload(localdir=None, remotedir=TARGET_WORKSPACE):
    upload_project(localdir, remotedir)