from defines import *
from battle import *
from register import *
from dbMapper import *

def testAttack():
    test_attack = 10
    test_defence = 4
    kick_damage = generate_kick(test_attack, test_defence)
    
    print("Атака: ", test_attack, " // Защита: ", test_defence)
    print("Удар на ", kick_damage, " урона.")
    
    test_attack = 10
    test_defence = 12
    kick_damage = generate_kick(test_attack, test_defence)
    
    print("Атака: ", test_attack, " // Защита: ", test_defence)
    print("Удар на ", kick_damage, " урона.")
    
    test_attack = 10
    test_defence = 9
    kick_damage = generate_kick(test_attack, test_defence)
    
    print("Атака: ", test_attack, " // Защита: ", test_defence)
    print("Удар на ", kick_damage, " урона.")
    

def main():
    connectDB()

    #test block start
    chat_id = 189974601
    #test block end

    if(existUser(chat_id) == USER_DOESNT_EXIST):
        print("User does not exist. Creating new user!");
        newUser(chat_id)
    else:
        _uid = loadInfo(chat_id);
        if(_uid == SUCCESS_ANSWER):
            print("Information successfully loaded. UID = %d", _uid);    

    
main()