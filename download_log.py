"""
_*_ coding:utf-8 _*_
_*_ author:iron_huang _*_
_*_ blog:https://www.dvpos.com/ _*_
"""

import paramiko
import os
import time
import common

local_miner_path = os.path.join(common.DOCS_PATH, common.LOCAL_MINER_NAME)
local_daemon_path = os.path.join(common.DOCS_PATH, common.LOCAL_DAEMON_NAME)


def exec_copy_cmd(scp):
    sftp = paramiko.SFTPClient.from_transport(scp)
    try:
        sftp.get(common.REMOTE_MINER_PATH, os.path.join(common.DOCS_PATH, local_miner_path))
        sftp.get(common.REMOTE_DAEMON_PATH, os.path.join(common.DOCS_PATH, local_daemon_path))
        scp.close()
        return "copy ok"
    except Exception as e:
        return e


def exec_make_log(pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=common.TARGET_IP, port=common.PORT, username=common.USER_NAME, password=pwd)
    cmd1 = 'cat miner.log | grep -a "attempting to mine a block" | grep "%s" > minerlog.log' % common.DATE_TO_RECORD
    cmd2 = 'cat daemon.log | grep -a "new block over pubsub" | grep "%s" > daemonlog.log' % common.DATE_TO_RECORD
    try:
        ssh.exec_command(cmd1)
        ssh.exec_command(cmd2)
    except Exception as e:
        return e


def init_scp(pwd):
    scp = paramiko.Transport(common.TARGET_IP, common.PORT)
    scp.connect(username=common.USER_NAME, password=pwd)
    return scp


def start_copy(pwd):
    err = exec_make_log(pwd)
    if err != None:
        return err
    else:
        scp = init_scp(pwd)
        if os.path.exists(local_miner_path):
            print("start del old miner file")
            os.remove(local_miner_path)
            print("del old miner file success")
        if os.path.exists(local_daemon_path):
            print("start del old daemon file")
            os.remove(local_daemon_path)
            print("del old daemon success")
    time.sleep(2)
    print("start copy new log file")
    msg = exec_copy_cmd(scp)
    print(msg)
