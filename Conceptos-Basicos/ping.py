import os

ips = [
    '192.168.0.1'
]

for ip in ips:
    res = os.popen(f"ping {ip}").read().strip()
    result_items = res.split("\n")
    print(result_items[1])
    print(result_items[2])
    print(result_items[3])
    print(result_items[4])
    