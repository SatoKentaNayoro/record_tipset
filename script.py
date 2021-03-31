"""
_*_ coding:utf-8 _*_
_*_ author:iron_huang _*_
_*_ blog:https://www.dvpos.com/ _*_
"""
import common
import json
import requests
import time
from datetime import datetime


def parse_time(t):
    before = t.split(".")[0].split("T")
    time_info = before[1]
    year_info, month_info, date_info = before[0].split("-")
    return year_info, month_info, date_info, time_info


def split_line_to_slice(file):
    line_to_slice = []
    for line in file:
        single = []
        moment = line.split("attempting to mine a block")
        tip_time = moment[0].split("\t")[0]
        if common.DATE_TO_RECORD not in tip_time:
            continue
        single.append(tip_time)
        single.append(json.loads(moment.pop()))
        line_to_slice.append(single)
    return line_to_slice


def get_set_location(diff, local_tip_sets):
    if diff in local_tip_sets:
        return "存在本地，远端无"
    else:
        return "存在远端，本地无"


def get_loc_new_block_time(diff, local_daemon_map):
    return local_daemon_map.get(diff)


def get_tipset_key(height):
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + common.TOKEN}
    params = {
        "jsonrpc": "2.0",
        "method": "Filecoin.ChainGetTipSetByHeight",
        "id": 1,
        "params": [
            height, None
        ]
    }
    r = requests.post(common.URL, headers=headers, json=params)

    if r.status_code == 200:
        result = r.json()["result"]["Cids"]
        return result


def get_block_header(cid):
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + common.TOKEN}
    params = {
        "jsonrpc": "2.0",
        "method": "Filecoin.ChainGetBlock",
        "id": 1,
        "params": [
            {"/": cid},
        ]
    }
    r = requests.post(common.URL, headers=headers, json=params)
    if r.status_code == 200:
        js = r.json()
        miner, time_stamp = js["result"]["Miner"], js["result"]["Timestamp"]
        time_array = time.localtime(time_stamp)
        time_remote = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        return miner, time_remote
    else:
        return None, None


def time_compare(loc_time, time_remote):
    if loc_time < time_remote:
        return common.LOC_BEFORE_REMOTE
    elif loc_time > time_remote:
        return common.LOC_AFTER_REMOTE
    else:
        return common.LOC_EQU_REMOTE


def reduce_time_str(time1, time2):
    t1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")
    return t1 - t2
