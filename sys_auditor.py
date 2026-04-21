import os

# Define the log location
log_path = "/var/log/sys_audit.log"

# Get the disk space usage (df -h)
# We use popen to capture the output of the command
disk_status = os.popen("df -h").read()

# Write the output to the log file
with open(log_path, "a") as log:
    log.write("--- SYSTEM AUDIT ---\n")
    log.write(disk_status)
    log.write("\n" + "="*20 + "\n")

print(f"Audit complete. Results written to {log_path}")
