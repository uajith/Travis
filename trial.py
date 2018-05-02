import subprocess
stdoutdata = subprocess.getoutput("wc --lines /var/log/syslog")
print("stdoutdata: " + stdoutdata.split()[0])
