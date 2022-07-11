import mail
from gui import message_box
from gui.main_window import get_user_pass

username, password = get_user_pass()
try:
    s_list,m_list = mail.post_details_connect_server(username, password)
except Exception as ep:
    message_box.message_box(str(ep), "error")
    message_box.message_box("Please Check Username and password "
                            , "error")
    message_box.message_box("Check your Internet Connectivity")
    print("----------    ERROR    -----------")
    print("\n")
    print(ep)
    print("\n")
    print("-----------------------------------")
    exit(1)
print("\n\n")
print("Working ON")
from learning.learning import test
y_preds = test(s_list)
print(y_preds)
ypreds=list(y_preds)

counter=1
for ypred,mlist in zip(ypreds,m_list):
    if ypred==1:
        message_box.message_box(f"Message {counter}:{mlist} is Spam")
    else:
        message_box.message_box(f"Message {counter}:{mlist} is Not Spam")
    counter+=1