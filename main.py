from defines import *
from battle import *
from register import *
from manageDBMapper import *
from dbMapper import connectDB


def main():
    connectDB()

    #test block start
    chat_id = "189974601"
    #test block end

    _uid = existUser(chat_id);

    if(_uid == USER_DOESNT_EXIST):
        print("User does not exist. Creating new user!");
        newUser(chat_id)
    else:
        _username = loadInfo(_uid);
        if(_username == USER_DOESNT_EXIST):
            print("User data does not exist. Reporting to administrator! Wait for feedback.");
        else:
            print("Information successfully loaded. Username is ", _username);    
            printLocation(_uid);


main()