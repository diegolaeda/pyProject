from dbMapper import *
from defines import *

def existUser(arg_chat_id):
    
    _exist = selectQuery("users", "uid", "telegram_id", arg_chat_id);
    #test down
    # _exist = False
    #test up
    
    print("_exist = ", _exist[0]);

    if(_exist != ""):
        return _exist[0];
    else:
        return USER_DOESNT_EXIST

def loadInfo(arg_uid):
    _hero_name = selectQuery("character_data", "hero_name", "character_id", str(arg_uid));

    if(_hero_name != ""):
        return _hero_name[0];
    else:
        return USER_DOESNT_EXIST;

def printLocation(arg_uid):
    _cur_location = complexQuery("SELECT loc.location_name, loc.location_desc, ch.hero_name"
                                " FROM character_data AS ch, locations AS loc"
                                " JOIN current_char_stats AS cur ON loc.location_id=cur.cur_location"
                                " WHERE cur.character_id = '"+str(arg_uid)+"';");

    _textPrint = "Сейчас ";
    _textPrint += _cur_location[2];
    _textPrint += " находится в локации ";
    _textPrint += _cur_location[0];
    _textPrint += " и читает внезапно появившуюся на экране его смартфона надпись: \" ";
    _textPrint += _cur_location[1];
    _textPrint += "\" ";
    print(_textPrint);