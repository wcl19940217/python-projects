import itchat
import time
import pandas as pd
import random
import re

def load_words(file_path):
    content = []
    with open(file_path,"r",encoding="utf-8") as f:
        con=f.readlines()
        con=[i.strip() for i in con]
        num=len(con)
        sentenses = pd.DataFrame(con, columns=["word"])
        print(sentenses)
        for i in range(num):
            if len(con[i])>0:
                message = re.split('\t',con[i])
                print(message)
                content.append(message[1].strip())
    return content

def get_userName():
    itchat.auto_login(hotReload=True)
    friend=itchat.search_friends(name="亭韵1")
    print(friend)
    userName = friend[0]['UserName']
    return userName

def send_msg(content,second):
    userName = get_userName()
    itchat.send("{}".format(random.choice(content)), toUserName=userName)
    time.sleep(second)
    send_msg(content,second)

file_path="sentenses.txt"
second=5
content=load_words(file_path)
send_msg(content,second)
