import json
import time
import sys
f = open("report.json", "r")
report = json.loads( f.read() )
report["uri"] = 'http://acme.org/1'
print json.dumps(report, sort_keys=True, indent=4, separators=(',', ': '))
sys.stdout.flush()
time.sleep(1)
report["uri"] = 'http://acme.org/2'
print json.dumps(report, sort_keys=True, indent=4, separators=(',', ': '))
sys.stdout.flush()
time.sleep(2)
report["uri"] = 'http://acme.org/3'
print json.dumps(report, sort_keys=True, indent=4, separators=(',', ': '))
sys.stdout.flush()
time.sleep(3)
