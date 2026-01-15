import subprocess
is_error_exc = False
def subprocess_run_pipeline(cmd):
    global is_error_exc
    if isinstance(cmd, list):
        cmd = " ".join(cmd)
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        stdout, stderr = process.communicate()
        if stderr:
            is_error_exc = True
            print(stderr)
    except OSError as er:
        is_error_exc = True
        print(f"OSError: {er}")
    return stdout

def main():
    print("----------------MANAGE USERS AND GROUPS----------------" "\n" "USERS:" "\n" + subprocess_run_pipeline(["cat /etc/passwd | grep -Ev 'nologin|false' | cut -d: -f1"]) + "\n" + "GROUPS:"+ subprocess_run_pipeline(["cat /etc/group | cut -d: -f1"]) +"\n" + "OPTIONS:" +"\n" + "%A for all users" + "\n" + "%U for new user" + "\n" + "%G for new group" + "\n" +"%B for adding multiple users to a group" "\n"+"%Q to exit" +"\n"+"------------------------------------------------------"+"\n")
    cc= input("$: ").upper()
    if cc == "%Q":
        exit()
    if cc == "%A":
        print(subprocess_run_pipeline(["cat /etc/passwd | cut -d: -f1"]))
    elif cc == "%U":
        userthingwierd= input("Enter new username: ")
        subprocess_run_pipeline(["sudo adduser", "--disabled-password", "--gecos", '""', userthingwierd]) 
        subprocess_run_pipeline([f"sudo mkdir /{userthingwierd}"]) #IDK WHY U ASKED FOR THIS BUT OK
        subprocess_run_pipeline(["sudo chmod", "1770", f"/{userthingwierd}"])
        subprocess_run_pipeline([f"sudo chown {userthingwierd}:{userthingwierd} /{userthingwierd}"])
        if input("Want to include in a group? (y/n): ").lower() == "y":
            groupthingwierd= input("Enter group name: ")
            subprocess_run_pipeline(["sudo groupadd", groupthingwierd]) 
            subprocess_run_pipeline(["sudo usermod", "-aG", groupthingwierd, userthingwierd])
    elif cc == "%G":
        groupthingwierd= input("Enter new group name: ")
        subprocess_run_pipeline(["sudo groupadd", groupthingwierd])
    elif cc == "%B":
        groupthingwierd= input("Enter group name: ")
        subprocess_run_pipeline(["sudo groupadd", groupthingwierd]) 
        userthingwierd2= input("Enter Users to add to group (comma separated): ")
        for user in userthingwierd2.split(","):
            subprocess_run_pipeline(["sudo useradd", user.strip(), "-G", groupthingwierd])
            subprocess_run_pipeline([f"sudo mkdir /{user.strip()}"])
            subprocess_run_pipeline(["sudo chmod", "1770", f"/{user.strip()}"])
            subprocess_run_pipeline([f"sudo chown {user.strip()}:{groupthingwierd} /{user.strip()}"])
    else:
        print("Invalid option selected.")
    print("DONE! Press Enter to continue...")
    input()
if __name__ == "__main__":
    # Ensure script is run as root
    out = subprocess_run_pipeline(["id -u"])
    if out.strip() != "0":
        print("This script must be run as root.")
        print(out)
    else:
        while True:
            main()