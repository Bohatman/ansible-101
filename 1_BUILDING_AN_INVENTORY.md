# Setup authorized_keys
1. Gen public key ```ssh-keygen```
2. Copy to remote host ```sh-copy-id username@remote_host```

** ```cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"```

# Create inventory
1. Create file ```inventory.ini```
2. Add new hosts with group [myhosts]
``` text
[myhosts]
192.168.1.43
```
3. List inventory ```ansible-inventory -i inventory.ini --list```
4. Ping to host ```ansible myhosts -m ping -i inventory.ini```
