import subprocess
is_error_exc = False
typex = False
def subprocess_run_pipeline(cmd):
    global is_error_exc
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        stdout, stderr = process.communicate()
        if typex:
            print(stdout)
        if stderr:
            is_error_exc = True
            print(stderr)
    except OSError as er:
        is_error_exc = True
        print(f"OSError: {er}")
    return stdout

def main():
    typex = True
    print("----------------MANAGE USERS AND GROUPS----------------" "\n" "USERS:" "\n" + subprocess_run_pipeline(["cat /etc/passwd | grep -Ev 'nologin|false' | cut -d: -f1"]) + "\n" + "GROUPS:"+ subprocess_run_pipeline(["cat /etc/group | cut -d: -f1"]) +"\n" + "OPTIONS:" +"\n" + "%A for all users" + "\n" + "%U for new user" + "\n" + "%G for new group" + "\n" +"%B for adding multiple users to a group" "\n"+"------------------------------------------------------"+"\n")
    if input("$: ") == "%A":
        print(subprocess_run_pipeline(["cat /etc/passwd | cut -d: -f1"]))
    elif input("$: ") == "%U":
        userthingwierd= input("Enter new username: ")
        subprocess_run_pipeline(["sudo adduser", userthingwierd]) 
        subprocess_run_pipeline([f"sudo mkdir /{userthingwierd}"]) #IDK WHY U ASKED FOR THIS BUT OK
        subprocess_run_pipeline(["sudo chmod", "1770", f"/{userthingwierd}"])
        subprocess_run_pipeline([f"sudo chown {userthingwierd} /{userthingwierd}"])
        if input.lower("Want to include in a group? (y/n): ") == "y":
            groupthingwierd= input("Enter group name: ")
            subprocess_run_pipeline(["sudo groupadd", groupthingwierd]) 
            subprocess_run_pipeline(["sudo usermod", "-aG", groupthingwierd, userthingwierd])
    elif input("$: ") == "%G":
        groupthingwierd= input("Enter new group name: ")
        subprocess_run_pipeline(["sudo groupadd", groupthingwierd])
    elif input("$: ") == "%B":
        groupthingwierd= input("Enter group name: ")
        subprocess_run_pipeline(["sudo groupadd", groupthingwierd]) 
        userthingwierd2= input("Enter Users to add to group (comma separated): ")
        for user in userthingwierd2.split(","):
            subprocess_run_pipeline(["sudo useradd", user.strip(), "-G", groupthingwierd])
    else:
        print("Invalid option selected.")
    input()
if __name__ == "__main__":
    # Ensure script is run as root
    out = subprocess_run_pipeline(["id -u"])
    if out.strip() != "0":
        print("This script must be run as root (sudo).")
        print(out)
    else:
        while True:
            main()
            print("DONE!")