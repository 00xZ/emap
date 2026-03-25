#Works better if looking for SSH servers only
import threading
import sys
import socket
import random

print("     ______                       ")
print("    / ____/  ____ _________  ____ ")
print("   / __/    / __ -__ |  __ -/ __ | ")
print("  / /___   / / / / / / /_/ / /_/ /")
print(" /_____/  /_/ /_/ /_/|__,_/ .___/ ")
print("                         /_/      ")
print("     github/00xZ - Eyezik")

# -------------------- CONFIG --------------------

port = int(sys.argv[1])
threads = int(sys.argv[2])
output_file = sys.argv[3]
amount_to_scan = int(sys.argv[4])

# Clear output file
open(output_file, 'w').close()

# Thread-safe counter + lock
lock = threading.Lock()
found = 0

def is_blacklisted(o1, o2, o3, o4):
    return (
        o1 == 127 or
        o1 == 0 or
        o1 == 3 or
        o1 in (15, 16, 56, 10, 25, 49, 50, 137) or
        o1 in (6, 7, 11, 21, 22, 26, 28, 29, 30, 33, 55, 214, 215) or

        (o1 == 192 and o2 == 168) or
        (o1 == 172 and 16 <= o2 < 32) or
        (o1 == 100 and 64 <= o2 < 127) or
        (o1 == 169 and o2 > 254) or
        (o1 == 198 and 18 <= o2 < 20) or

        (o1 == 146 and o2 in (17, 80, 98, 154)) or
        (o1 == 147 and o2 == 159) or
        (o1 == 148 and o2 == 114) or
        (o1 == 150 and o2 in (125, 133, 144, 149, 157, 184, 190, 196)) or
        (o1 == 152 and o2 in (82, 229)) or
        (o1 == 157 and o2 in (202, 217)) or
        (o1 == 161 and o2 == 124) or
        (o1 == 162 and o2 == 32) or
        (o1 == 155 and o2 in (96, 149, 155, 178)) or
        (o1 == 164 and o2 == 158) or
        (o1 == 156 and o2 == 9) or
        (o1 == 167 and o2 == 44) or
        (o1 == 168 and o2 in (68, 85, 102)) or
        (o1 == 203 and o2 == 59) or
        (o1 == 204 and o2 == 34) or
        (o1 == 207 and o2 in (30, 120)) or
        (o1 == 117 and o2 in (55, 56)) or
        (o1 == 80 and o2 == 235) or
        (o1 == 209 and o2 == 35) or

        # Large range rules
        (o1 == 64 and (o2 == 70 or 69 <= o2 < 227 or 224 <= o2 < 227)) or
        (o1 == 128 and 35 <= o2 < 237) or
        (o1 == 129 and 22 <= o2 < 255) or
        (o1 == 130 and 40 <= o2 < 168) or
        (o1 == 131 and 3 <= o2 < 251) or
        (o1 == 132 and 3 <= o2 < 251) or
        (o1 == 134 and 5 <= o2 < 235) or
        (o1 == 136 and 177 <= o2 < 223) or
        (o1 == 138 and 13 <= o2 < 194) or
        (o1 == 139 and 31 <= o2 < 143) or
        (o1 == 140 and 1 <= o2 < 203) or
        (o1 == 143 and 45 <= o2 < 233) or
        (o1 == 144 and 99 <= o2 < 253) or

        (o1 == 147 and (
            35 <= o2 < 43 or
            103 <= o2 < 105 or
            168 <= o2 < 170 or
            198 <= o2 < 200 or
            238 <= o2 < 255
        )) or

        (o1 == 150 and 113 <= o2 < 115) or
        (o1 == 152 and 151 <= o2 < 155) or
        (o1 == 153 and 21 <= o2 < 32) or
        (o1 == 155 and (
            5 <= o2 < 10 or
            74 <= o2 < 89 or
            213 <= o2 < 222
        )) or
        (o1 == 157 and 150 <= o2 < 154) or
        (o1 == 158 and (1 <= o2 < 21 or 235 <= o2 < 247)) or
        (o1 == 159 and 120 <= o2 < 121) or
        (o1 == 160 and 132 <= o2 < 151) or

        # Gov / special
        (o1 == 162 and 45 <= o2 < 47) or
        (o1 == 163 and 205 <= o2 < 207) or
        (o1 == 164 and (45 <= o2 < 50 or 217 <= o2 < 233)) or
        (o1 == 169 and 252 <= o2 < 254) or
        (o1 == 199 and 121 <= o2 < 254) or
        (o1 == 205 and 1 <= o2 < 118) or
        (o1 == 207 and 60 <= o2 < 62) or

        # Cloudflare
        (o1 == 104 and 16 <= o2 < 31) or

        # Digital Ocean (subset)
        (o1 == 188 and o2 in (166, 226)) or
        (o1 == 159 and o2 == 203) or
        (o1 == 162 and o2 == 243) or
        (o1 == 45 and o2 in (55, 76, 63)) or
        (o1 == 178 and o2 == 62) or

        # Amazon / Microsoft
        (o1 == 107 and 20 <= o2 < 24) or
        (o1 == 35 and 159 <= o2 < 183) or
        (o1 == 52) or
        (o1 == 54 and (64 <= o2 < 95 or 144 <= o2 < 255)) or
        (o1 == 13 and (52 <= o2 < 60 or 112 <= o2 < 115)) or

        # ONLINE SAS
        (o1 == 163 and o2 == 172) or
        (o1 == 51 and 15 <= o2 < 255) or

        # Misc
        (o1 == 79 and o2 == 121 and 128 <= o3 < 255) or
        (o1 == 212 and o2 == 47 and 224 <= o3 < 255) or
        (o1 == 89 and o2 == 34 and 96 <= o3 < 97) or
        (o1 == 219 and 216 <= o2 < 231) or
        (o1 == 23 and 94 <= o2 < 109) or
        (o1 == 106 and (182 <= o2 < 189 or o2 >= 184)) or
        (o1 == 34 and 245 <= o2 < 255) or
        (o1 == 87 and 97 <= o2 < 99) or
        (o1 == 86 and o2 in (208, 209)) or
        (o1 == 193 and o2 == 164) or
        (o1 == 120 and 103 <= o2 < 108) or
        (o1 == 188 and o2 == 68) or
        (o1 == 78 and o2 == 46) or

        # Multicast
        (o1 >= 224)
    )


def ssh_scan():
    global found

    while True:
        with lock:
            if found >= amount_to_scan:
                return

        # Generate random IP
        o1 = random.randint(1, 254)
        o2 = random.randint(1, 254)
        o3 = random.randint(1, 254)
        o4 = random.randint(1, 254)

        if is_blacklisted(o1, o2, o3, o4):
            continue

        ip = f"{o1}.{o2}.{o3}.{o4}"

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((ip, port))

            banner = sock.recv(1024).decode(errors="ignore")

            if banner.startswith("SSH-"):
                with lock:
                    if found < amount_to_scan:
                        print(f"[✓] SSH found: {ip}")
                        with open(output_file, "a") as f:
                            f.write(ip + "\n")
                        found += 1

            sock.close()

        except:
            pass

thread_list = []

for _ in range(threads):
    t = threading.Thread(target=scan)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print(f"\n[ Done | Found: {found} SSH hosts ]")
