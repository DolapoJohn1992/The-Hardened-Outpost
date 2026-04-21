import os

# Configuration
DC_IP = "10.0.0.X"  # <--- Change this to your Windows DC IP
LOG_FILE = "/var/log/dc_audit.log"

# Ping the DC 4 times
# -c 4 sends 4 packets
response = os.system(f"ping -c 4 {DC_IP} > /dev/null 2>&1")

# Write results to the log
with open(LOG_FILE, "a") as log:
    if response == 0:
        log.write("DC is UP\n")
    else:
        log.write("DC is DOWN\n")
