import datetime
import time
#Put this file in C drive
end_time=datetime.datetime(2024,2,5)
site_block=["www.facebook.com"]
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"
while True:
    if datetime.datetime.now() < end_time:
        print("start blocking")
        with open(host_path,"r+") as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect +" "+website+"\n")
                else:
                    pass
    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)