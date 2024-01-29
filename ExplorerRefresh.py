from subprocess import call
import time
import datetime

curtime = datetime.datetime.now()
while True:
    time.sleep(1)
    diff = (datetime.datetime.now() - curtime).total_seconds()
    print(diff)
    if diff > 1:
        call("taskkill /IM explorer.exe /F", shell=True)
        call(["start", "explorer.exe"], shell=True)
        break
    curtime = datetime.datetime.now()
