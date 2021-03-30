#!/usr/bin/python3
# coding=utf-8
"""
Function:
    1. Execute Linux command via remote SSH
    2. Capture Interface info to MySQL server
    3. Copy file to MySQL server '/tmp' via sftp
Support: CentOS6, 7, Raspbian9.4
Capture: ManageIP, portID, MTU, MAC, IPv4,
         IPv6, DS-lite Remote IP, DS-lite Local IP,
         Hostname, System, Kernel
History:
    9/24/2020 deliangw: create
    10/10/2020 deliangw:  add system version check & server IP select
                        & table exist check & capture Hostname, System, Kernel info
    10/11/2020 deliangw: check code format
    10/12/2020 deliangw: split IPv6 link local & global address
    10/15/2020 deliangw: support Raspbian 9.4
"""
import wmi
import pymysql      # MySQL of Python3
import paramiko
import re
#import couchdb
# import random
global SQLServer, SQLUser, SQL_PWD, sftpServer

ssh = paramiko.SSHClient()  # Create SSH object
#Server_IP = '135.251.192.220'
Server_IP = '192.168.3.30'
#Server_IP = '192.168.3.188'

if Server_IP == '192.168.3.30':
    SSHLoginUser = 'root'
    SSHLoginPWD = 'ad9741'
    SQLServer = '192.168.3.30'
    SQLUser = 'root'
    SQL_PWD = '123456'
    sftpServer = '192.168.3.30'
    sftpPWD = 'ad9741'
elif Server_IP == '192.168.3.188':
    SSHLoginUser = 'root'
    SSHLoginPWD = '123456'
    SQLServer = '192.168.3.188'
    SQLUser = 'root'
    SQL_PWD = '123456'
    sftpServer = '192.168.3.188'
    sftpPWD = '123456'
elif Server_IP == '135.251.192.220':
    SSHLoginUser = 'root'
    SSHLoginPWD = 'NSB1234!'
    SQLServer = '135.251.192.220'
    SQLUser = 'root'
    SQL_PWD = '123456'
    sftpServer = '135.251.192.220'
    sftpPWD = 'NSB1234!'


# noinspection PyTypeChecker
def sftp_put(sftp_server):  # put file from windows to Linux
    transport = paramiko.Transport((sftp_server, 22))
    transport.connect(username=SSHLoginUser, password=sftpPWD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    remote_file = r'/tmp/GetInterfaceInfo.py'
    #local_file = r'D:\python\ServerAccess\GetInterfaceInfo.py'
    local_file = r'E:\python\GetInterfaceInfo.py'
    sftp.put(local_file, remote_file)  # put *.py to /tmp
    transport.close()


def ssh_conn():
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())  # Allow connect to host that not in file ~/.ssh/known_hosts
    ssh.connect(hostname=Server_IP, port=22, username=SSHLoginUser, password=SSHLoginPWD)  # Connect to Server


def ssh_dis_conn():
    ssh.close()  # Close SSH connect


# noinspection PyGlobalUndefined
def ssh_cmd(cmd_in, cmd_type):
    global res, err
    stdin, stdout, stderr = ssh.exec_command(cmd_in)  # Run command
    if cmd_type == 'read':  # Read command type is string
        res, err = stdout.read(), stderr.read()
    elif cmd_type == 'readlines':  # Read command type is list
        res, err = stdout.readlines(), stderr.read()
    elif cmd_type == 'readline':  # Read command type is string
        res, err = stdout.readline(), stderr.read()
    result = res if res else err
    res = result
    return res  # Return res value


def create_database(database_name):
    create_cmd = "CREATE DATABASE " + database_name + ";"
    cur.execute(create_cmd)


def delete_table_entry(ip):
    delete_cmd = "delete from Interface where ManageIP = '" + ip + "';"
    cur.execute(delete_cmd)


def create_table():
    cur.execute(
        "create table Interface(ManageIP varchar(15),portID varchar(20),mtu varchar(5),MAC varchar(17),"
        "IPv4 varchar(15),IPv6_LinkLocal varchar(30),IPv6_Global varchar(30),Remote varchar(40),Local varchar(40),"
        "Hostname varchar(40),System varchar(40),Kernel varchar(40));")


def insert_table(*info):  # Insert interface info to MySQL
    sql = "insert into Interface values("
    sql1 = "insert into Interface values"
    sql2 = "("
    for I in info:
        if I != info[-1]:
            sql = sql + "%s,"
            sql2 = sql2 + '\'' + I + '\','
        else:
            sql = sql + "%s"
            sql2 = sql2 + '\'' + I + '\')'
    sql3 = sql1 + sql2
    cur.execute(sql3)


def system():
    system_cmd = 'cat /etc/issue |awk \'{print $1}\''
    version = ssh_cmd(system_cmd, 'readline')
    # print(type(version),version)
    return version


def system_version_centos():
    version_cmd = 'cat /etc/redhat-release |sed \'s/release /\\n/g\' | grep -v ^$ |awk \'{print $1}\''
    version = ssh_cmd(version_cmd, 'readlines')
    version = version[1]
    return version

'''
def system_version_windows(ipaddress, user, password):
    conn_win = wmi.WMI(computer=ipaddress, user=user, password=password)
    for sys in conn_win.Win32_OperatingSystem():
        print "Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber  #系统信息
        print sys.OSArchitecture.encode("UTF8")  # 系统的位数
        print sys.NumberOfProcesses  # 系统的进程数
'''

def ports_number():
    global interface
    version = system_version_centos()
    if "CentOS" in system():
        if version[0] == '6':
            cmd = 'ifconfig | grep encap | cut -d \' \' -f 1'  # Capture network ports number of Centos6
        elif version[0] == '7':
            cmd = 'ifconfig | grep flags | cut -d \':\' -f 1'  # Capture network ports number of Centos7
        interface = ssh_cmd(cmd, 'readlines')  # Run cmd via remote ssh
    elif "Raspbian" in system():
        cmd = 'ifconfig | grep flags | cut -d \':\' -f 1'  # Capture network ports number of Raspbian
    interface = ssh_cmd(cmd, 'readlines')  # Run cmd via remote ssh
    #print(interface)
    return interface


def cmd_centos(i):
    global cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10
    version = system_version_centos()
    if "CentOS" in system():
        cmd9 = 'cat /etc/redhat-release |awk \'{print $0}\''  # System
        cmd10 = 'uname -r'  # Kernel
        if version[0] == '6':  # When version is Centos6
            cmd1 = 'ifconfig |grep ' + interface[i].strip('\n') + ' | cut -d \' \' -f 1'  # port ID
            # cmd2 = 'ifconfig |grep ' + interface[i].strip('\n') + ' -A 5 |grep \'mtu\' | cut -d \' \' -f 16'  # mtu
            cmd2 = 'ifconfig | grep eth1 -A 5 | grep \'MTU\' | cut -d \':\' -f 2 | awk \'{print $1}\''
            # print(cmd2)
            cmd3 = 'ifconfig |grep ' + interface[i].strip('\n') + ' | cut -d \' \' -f 11'  # MAC address
            cmd4 = 'ifconfig |grep ' + interface[i].strip(
                '\n') + ' -A 2 |grep \'inet \' |cut -d \' \' -f 12'  # IPv4
            cmd5 = 'ifconfig |grep ' + interface[i].strip(
                '\n') + ' -A 3 |grep inet6 |awk \'{print $3}\''  # IPv6
            cmd6 = 'ip -6 tunnel |grep ' + interface[i].strip(
                '\n') + ' |cut -d \' \' -f 4'  # IPv6 DS-lite remote IP
            cmd7 = 'ip -6 tunnel |grep ' + interface[i].strip(
                '\n') + ' |cut -d \' \' -f 6'  # IPv6 DS-lite local IP
            cmd8 = 'hostname'  # Hostname
        elif version[0] == '7':  # When version is Centos7
            cmd1 = 'ifconfig |grep ' + interface[i].strip('\n') + ' | cut -d \':\' -f 1'  # port ID
            cmd2 = 'ifconfig |grep ' + interface[i].strip('\n') + ' | awk \'{print $4}\''  # mtu
            cmd3 = 'ifconfig |grep ' + interface[i].strip(
                '\n') + ' -A 5 |grep \'ether\' |cut -d \' \' -f 10'  # MAC address
            cmd4 = 'ifconfig |grep ' + interface[i].strip(
                '\n') + ' -A 2 |grep \'inet \' |cut -d \' \' -f 10'  # IPv4
            cmd5 = 'ifconfig |grep ' + interface[i].strip(
                '\n') + ' -A 3 |grep inet6 |cut -d \' \' -f 10'  # IPv6
            cmd6 = 'ip -6 tunnel |grep ' + interface[i].strip(
                '\n') + ' |cut -d \' \' -f 4'  # IPv6 DS-lite remote IP
            cmd7 = 'ip -6 tunnel |grep ' + interface[i].strip(
                '\n') + ' |cut -d \' \' -f 6'  # IPv6 DS-lite local IP
            cmd8 = 'hostnamectl |grep \'Static hostname\' | awk \'{print $3}\''  # Hostname
    return cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10


def cmd_raspbian(i):
    global cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10
    if "Raspbian" in system():
        cmd1 = 'ifconfig |grep ' + interface[i].strip('\n') + ' | cut -d \':\' -f 1'  # port ID
        cmd2 = 'ifconfig |grep ' + interface[i].strip('\n') + ' | awk \'{print $4}\''  # mtu
        cmd3 = 'ifconfig |grep ' + interface[i].strip(
            '\n') + ' -A 5 |grep \'ether\' |cut -d \' \' -f 10'  # MAC address
        cmd4 = 'ifconfig |grep ' + interface[i].strip(
            '\n') + ' -A 2 |grep \'inet \' |cut -d \' \' -f 10'  # IPv4
        cmd5 = 'ifconfig |grep ' + interface[i].strip('\n') + ' -A 3 |grep inet6 |cut -d \' \' -f 10'  # IPv6
        cmd6 = 'ip -6 tunnel |grep ' + interface[i].strip(
            '\n') + ' |cut -d \' \' -f 4'  # IPv6 DS-lite remote IP
        cmd7 = 'ip -6 tunnel |grep ' + interface[i].strip('\n') + ' |cut -d \' \' -f 6'  # IPv6 DS-lite local IP
        cmd8 = 'hostnamectl |grep \'Static hostname\' | awk \'{print $3}\''  # Hostname
        cmd9 = 'lsb_release -d |cut -d \':\' -f 2'  # System
        cmd10 = 'uname -r'  # Kernel
        return cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10


def capture_interface_info(manage_ip):
    global server_ip_str, port_id_str, mtu_str, mac_str, ipv4_str, ipv6_ll_str, ipv6_g_str, dsliter_str,\
        dslitel_str, hostname_str, system_str, kernel_str
    server_ip_str = str(manage_ip)  # Manage IP
    port_id_list = ssh_cmd(str(cmd1), 'readlines')
    port_id_str = ''.join(port_id_list).strip('\n')
    mtu_list = ssh_cmd(str(cmd2), 'readlines')
    mtu_str = ''.join(mtu_list).strip('\n').strip('mtu:')
    mac_list = ssh_cmd(str(cmd3), 'readlines')
    mac_str = ''.join(mac_list).strip('mtu:')
    ipv4_list = ssh_cmd(str(cmd4), 'readlines')
    ipv4_str = ''.join(ipv4_list).strip('mtu:').strip('addr:')
    ipv6_list = ssh_cmd(cmd5, 'readlines')
    ipv6_ll_str = ''
    ipv6_g_str = ''
    for j in range(len(ipv6_list)):
        ipv6_list[j] = ipv6_list[j].strip('\n')  # strip \n between multi IPv6 address
        str_ipv6 = ipv6_list[j]
        if str_ipv6[:4] == 'fe80':  # Check link local IPv6 address
            ipv6_ll_str = str_ipv6
        else:  # Check global IPv6 address
            ipv6_g_str = str_ipv6
    dsliter_list = ssh_cmd(str(cmd6), 'readlines')
    dsliter_str = ''.join(dsliter_list).strip('\n')
    dslitel_list = ssh_cmd(str(cmd7), 'readlines')
    dslitel_str = ''.join(dslitel_list).strip('\n')
    hostname_list = ssh_cmd(str(cmd8), 'readlines')
    hostname_str = ''.join(hostname_list).strip('\n')
    system_list = ssh_cmd(str(cmd9), 'readlines')
    system_str = ''.join(system_list).strip('\n')
    kernel_list = ssh_cmd(str(cmd10), 'readlines')
    kernel_str = ''.join(kernel_list).strip('\n')
    print(server_ip_str, port_id_str, mtu_str, mac_str, ipv4_str, ipv6_ll_str, ipv6_g_str, dsliter_str,
          dslitel_str, hostname_str, system_str, kernel_str)
    return server_ip_str, port_id_str, mtu_str, mac_str, ipv4_str, ipv6_ll_str, ipv6_g_str, dsliter_str,\
           dslitel_str, hostname_str, system_str, kernel_str

def update_table(manage_ip):
    ssh_conn()
    ports_number()
    for i in range(len(interface)):  # Capture info for all ports
        if interface[i] != 'lo\n':  # exclude lo port
            if "CentOS" in system():
                cmd_centos(i)
            elif "Raspbian" in system():
                cmd_raspbian(i)
            capture_interface_info(manage_ip)
            insert_table(server_ip_str, port_id_str, mtu_str, mac_str, ipv4_str, ipv6_ll_str, ipv6_g_str, dsliter_str,
                         dslitel_str, hostname_str, system_str, kernel_str)
    ssh_dis_conn()


if __name__ == "__main__":
    #system_version_windows(Server_IP, "shirley", "ad9741")
    conn = pymysql.connect(host=SQLServer, user=SQLUser, passwd=SQL_PWD, database="ServerInfo")   # define MySQL's parameters
    cur = conn.cursor()

    #create_database("ServerInfo")
    cur.execute("DROP TABLE IF EXISTS Interface")
    create_table()
    delete_table_entry(Server_IP)
    update_table(Server_IP)
    sftp_put(sftpServer)

    cur.close()
    conn.commit()
    conn.close()