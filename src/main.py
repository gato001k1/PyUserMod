import argparse
import subprocess
import sys
import os
import math
import json
import re

is_error_exc = False
def subprocess_run_pipeline(cmd):
    global is_error_exc
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

groupthingwierd= input("Enter group name: ")
subprocess_run_pipeline(["groupadd", groupthingwierd]) 
userthingwierd2= input("Enter Users to add to group (comma separated): ")
subprocess_run_pipeline(["useradd", userthingwierd2, "-G", groupthingwierd]) 
fifipasswd=input("Enter password for user: ")
subprocess_run_pipeline(["passwd", userthingwierd2, fifipasswd])
subprocess_run_pipeline(["sudo, usermod, -aGe", groupthingwierd, userthingwierd2])
filethingy= userthingwierd2
subprocess_run_pipeline(["sudo mkdir /", filethingy])
subprocess_run_pipeline(["sudo chown", userthingwierd2, filethingy])











































#        if process.returncode != 0:
#            print(f"Error: {stderr}")
#            is_error_exc = True
#            return stderr
#        else:
#            print(f"Output: {stdout}")
#            return stdout
#    except Exception as e:
#        print(f"Exception: {e}")
#        is_error_exc = True
#        return str(e)
#
#def create_group(group_name):
#    result = subprocess.run(
#        ["groupadd", group_name],
#        stdout=subprocess.PIPE,
#        stderr=subprocess.PIPE,
#        text=True
#    )
#    
#    if result.returncode == 0:
#        print(f"Group '{group_name}' created successfully.")
#        return True
#    else:
#        print(f"Failed to create group '{group_name}'.")
#        print(f"Error: {result.stderr}")
#        return False
#
#
## --- Main Program ---
#if __name__ == "__main__":
#    new_group_name = input()
#    
#    # Check for root privileges
#    uid = subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip()
#    
#    if uid != '0':
#        print("Error: This script must be run as root or with 'sudo'.")
#        sys.exit(1)
#    
#    print(f"Creating group: {new_group_name}")
#    create_group(new_group_name)
#




