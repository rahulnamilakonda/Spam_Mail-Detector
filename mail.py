import email
import logging
import poplib
import string
from email.parser import Parser
from io import StringIO
pserver=None

SERVER = "pop.gmail.com"
USER = None
PASSWORD = None
PORT='995'
def post_details_connect_server(user, password):
    global SERVER
    SERVER = "pop.gmail.com"
    global USER
    USER = user
    global PASSWORD
    PASSWORD = password
    msg_list=connect_server(USER, PASSWORD)
    return  msg_list


def connect_server(USER, PASSWORD, SERVER="pop.gmail.com"):
    # connect to server
    logging.debug('connecting to ' + SERVER)
    global pserver
    pserver = poplib.POP3_SSL(SERVER,PORT)
    # server = poplib.POP3(SERVER)
    # log in
    logging.debug('log in')
    pserver.user(USER)
    pserver.pass_(PASSWORD)
    # list items on server
    logging.debug('listing emails')
    resp, mails, octets = pserver.list()
    index=len(mails)
    # download the first message in the list
    # id, size = str.split(str(mails[0]))
    # print(id)
    # print(type(id))
    msg_list=[]
    msg_from=[]
    for i in range(1,index+1):
        resp, lines, octets = pserver.retr(i)
        msg_content=b'\r\n'.join(lines).decode('utf-8')
        msg=Parser().parsestr(msg_content)
        # print(msg.get('From'))
        # print(msg.get('Subject'))
        # print(msg.get('Date'))
        msg_list.append(msg.get('Subject'))
        msg_from.append(msg.get('From'))
    return msg_list,msg_from

# s_list=post_details_connect_server('rahulnamilakonda100@gmail.com','wvficbphcolgcarm')
# print(s_list)