from datetime import datetime

print("Hello World")
ipaddress = "192.168.178.100"
ipaddress = ipaddress.replace(".", "/")
print(ipaddress)

log_time = f"{datetime.now()}"

log_time = log_time.replace(" ", "_")
log_time = log_time.replace(":", "-")
log_time = log_time.replace(".", "-")
print(log_time)
