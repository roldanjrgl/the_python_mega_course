import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path= "/etc/hosts"
redirects = "127.0.0.1"
website_lists = ["www.facebook.com", "facebok.com", "www.youtube.com" , "www.twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print("Working hours...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            print(content)
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirects + " " + website + "\n")
    else:
        with open(hosts_path, "r+")  as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            
            file.truncate()
            
        print("Fun hours...")

    time.sleep(5)
