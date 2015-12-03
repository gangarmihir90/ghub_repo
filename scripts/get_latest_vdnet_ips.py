import os

files = os.popen('ls -lt /tmp/vdnet').read().splitlines()
for line in files:
    if line.startswith('total'):
        continue
    elif 'nsx-sdk' in line:
        continue
    else:
        latest_file = line.split()[-1]
        os.system('grep "ip address" /tmp/vdnet/%s/vdnet.log' % latest_file)
        break
