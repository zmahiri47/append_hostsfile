# Requirements

   * Python 3.7
   * python-hosts 1.0.5
   * argparse 1.4.0

# Setup

This script add entries to a Linux hostfile which requires sudo privileges.  To run script, as `root`, first run `pip installl -U requirements.txt`, then run he script with the default file, or supply a user-defined list of hosts in the following format

```
ip <adress> <hostname1> <hostname1>.fqdn
ip <adress> <hostname2> <hostname2>.fqdn
ip <adress> <hostname3> <hostname3>.fqdn
...
```

# Sample Execution & Output

If run without command line arguments, using

```
python ./append_hostfile.py
```

The script explanation of usage is available by using the `--help` flag

```
python ./append_hostfile.py --help
usage: append_hostfile.py
         [-h] [-f FILE]

Simple script to add host to Linux
hostfile

options:
  -h, --help      show this help
                  message and exit
  -f FILE, --file FILE
                  File used to add
                  entries to 
                  /etc/hosts (default:
                  hosts_to_add.txt)
```