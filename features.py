#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
from datetime import datetime

ipDict = {}
allDevices = {}
devices = []
def ipFeature(line):
    start, end, ip, device, identity = line.split(";")
    ip = ip.strip()
    ip1, ip2, ip3, ip4 = [int(x) for x in ip.split(".")]
    vec = [0]* (255*4)
    vec[ip1] = 1
    vec[ip2 + 255] = 1
    vec[ip3 + 255] = 1
    vec[ip4 + 255] = 1
    return vec

def timeStartFeature(line):
    start, end, ip, device, identity = line.split(";")
    hour, minute, sec = [int(x) for x in start.strip().split(":")]

    vect = [0] * 144
    vect[hour] = 1
    vect[24 + minute] = 1
    vect[84 + sec] = 1
    return vect

def timeEndFeature(line):
    start, end, ip, device, identity = line.split(";")
    hour, minute, sec = [int(x) for x in end.strip().split(":")]

    vect = [0] * 144
    vect[hour] = 1
    vect[24 + minute] = 1
    vect[84 + sec] = 1
    return vect

def device(line):
    start, end, ip, device, identity = line.split(";")
    device = device.strip()

    devices.append(device)
    
    # This is the index of device
    if device in allDevices:
        return allDevices[device]
    else:
        allDevices[device] = len(devices) - 1
        return allDevices[device]

def duration(line):
    start, end, ip, device, identity = line.split(";")
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end.strip(), FMT) - datetime.strptime(start.strip(), FMT)
    return tdelta.seconds/60

def durationLessThanMinute(line):
    return duration(line) < 1

def durationOneToFive(line):
    minutes = duration(line)
    return minutes > 0 and minutes < 5

def durationFiveOrMore(line):
    minutes = duration(line)
    return minutes >= 5
