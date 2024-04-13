#!/usr/bin/env python3

import os
from python_hosts import Hosts, HostsEntry
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
warnings.simplefilter("ignore")

def file_w_hosts_to_add(filename = 'hosts_to_add.txt'):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    file_w_hosts_to_add = os.path.join(__location__, filename)

    return file_w_hosts_to_add

def check_host(address_var):
    hosts = Hosts()
    if hosts.exists(address=address_var) == True:
        return True
    else:
        return False

def add_new_host(address_var, names_list: list[str], entry_type_var = 'ipv4'):
    hosts = Hosts()
    new_entry = HostsEntry(entry_type=entry_type_var, address=address_var, names=names_list)
    hosts.add([new_entry])
    print("Writing new host %s to /etc/hosts" % names_list[0])
    hosts.write()

if __name__ == "__main__":

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, description='Simple script to add hosts to Linux hostsfile')
    parser.add_argument("-f", "--file", default="hosts_to_add.txt", help="File used to add entries to /etc/hosts")
    args = parser.parse_args()

    hosts_to_add_path = file_w_hosts_to_add(filename= args.file)
    print("Using entries in %s to add hosts" % hosts_to_add_path)

    with open(hosts_to_add_path, 'r') as f:
        hosts_to_add_lines = [i.strip().split() for i in f]
        for line in hosts_to_add_lines:
            if len(line) != 3:
                continue
            else:
                if check_host(line[0]) == True:
                    print("%s already exists in /etc/hosts!" % line[0])
                else:
                    add_new_host(address_var=str(line[0]), names_list=line[1:3])


    