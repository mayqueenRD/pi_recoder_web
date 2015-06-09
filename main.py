#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import subprocess
import sys
import os
import time

app = Flask(__name__)

@app.route("/",methods=['GET' , 'POST'])
def main():
    disk_size=list()
    proc = subprocess.Popen(['./mnt_home','-c'], stdout=subprocess.PIPE)
    time.sleep(1)
    sc = open('./disk_list', 'r')
    for line in sc.readlines():
        disk_size.append(line.split("\n"))

    sc.close()
    templateData = {
        'disk_size': disk_size
    }

    return render_template('index.html',**templateData)

@app.route("/<mount>" ,methods=['GET' , 'POST'])
def mount(mount):
    disk_size=list()
    proc = subprocess.Popen(['./mnt_home','-c'], stdout=subprocess.PIPE)

    time.sleep(1)
    sc = open('./disk_list', 'r')
    for line in sc.readlines():
        disk_size.append(line.split("\n"))
    sc.close()

    mnt_disk=request.form['mnt_disk']
    proc = subprocess.Popen(["./mnt_home -m %s" % mnt_disk, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    message=out
    templateData = {
        'disk_size': disk_size,
        'message'  : message
    }

    return render_template('index.html',**templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
