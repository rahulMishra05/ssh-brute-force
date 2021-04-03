# SSH Brute Force

### 📝 About project
This is a python script written using python3. It can be used to find the password of a ssh client using brute force attack.\
First you have to enter the IP address of the host server or SSH server. Than you need to enter the username of the host whose password you want to guess. In the last step you have to enter the file name of the password list, for your help some common password list is provided, you can find them in `/password-list` directory.

**What is SSH and SSH client ?**\
The *Secure Shell Protocol* is a cryptographic network protocol for operating networks services securely over an unsecured network. Typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.\
SSH client is a program that allows establishing a secure and authenticated SSH connections to SSH server.

**What is brute force attack ?**\
A brute force attack consists of an attacker submitting many paswwords or passphrases with the hope of eventually guessing a combination correctly. The attacker systematically checks all possible passwords and passphrases until the correct one is found.

### 🗂 Libraries used 
1. **Paramiko:** Paramiko is a Python (2.7, 3.4+) implementation of the SSHv2 protocol [1], providing both client and server functionality. While it leverages a Python C extension for low level cryptography (Cryptography), Paramiko itself is a pure Python interface around SSH networking concepts.\
In this project this library is used to automate the process of connecting to SSH server.
2. **Sys:** The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.
3. **OS:** The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os. path* modules include many functions to interact with the file system
4. **Socket:** The Python interface is a straightforward transliteration of the Unix system call and library interface for sockets to Python’s object-oriented style: the socket() function returns a socket object whose methods implement the various socket system calls. Parameter types are somewhat higher-level than in the C interface: as with read() and write() operations on Python files, buffer allocation on receive operations is automatic, and buffer length is implicit on send operations.
5. **Tremcolor:** This module is used to print coloured ASCII characters on the terminal in output.
6. **Threading:**  A thread is a single sequential flow of control within a program. The real excitement surrounding threads is not about a single sequential thread. Rather, it's about the use of multiple threads running at the same time and performing different tasks in a single program.\
Threading module is used for creating, controlling and managing threads in python. This module is used because the password checking of the script was very slow and we have to increase the speed of checking passwords.
7. **Time:** The Python time module provides many ways of representing time in code, such as objects, numbers, and strings. It also provides functionality other than representing time, like waiting during code execution and measuring the efficiency of your code. This module is used because the password checking of the script was very slow and we have to increase the speed of checking passwords.

### 🧱 How to use 
1. First you have to clone/download this repository, you can do that by executing this command in terminal.
    ```shell
    git clone https://github.com/rahulMishra05/ssh-brute-force.git
    ```
2. Than change the working directory, and go to project directory.
    ```shell
    cd ssh-brute-force
    ```
3. Now if you use ls command than you can see all the files present in this directory. Among them file named `ssh_brute_force.py` is the main file/script.
4. To execute this script use this command.
    ```shell
    python3 ssh_brute_force.py
    ```
5. Than it will prompt a message like this
    ```shell
    [+] Target Address:
    ```
    Here you have to enter the IP address of the SSH server or host server.
6. After this you will get another message like this
    ```shell
    [+] SSH Username:
    ```
    Here you have to enter the username of the host, whose password you want to find.
7. Than a last message will appear, which will look something like this
    ```shell
    [+] Passwords File:
    ```
    Here you have to enter the location/name of the file which consists of list of passwords.
8. There is a folder/directory in this repository contaning the lists of passwords, name of that folder/directory is `/password-list`. It contains various password lists compressed usign a tool gzip, in order to use those list in the program you have to unzip thess files, and you can do that by executing a command like this.
    ```shell
    gzip -d top-20-common-SSH-passwords.txt.gz
    ```
