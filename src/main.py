import argparse
import subprocess



def subprocess_run_pipeline(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode()}")
    else:
        print(f"Output: {stdout.decode()}")


def main():
    
