import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from defines import *

def connectDB():
    connection = psycopg2.connect(user=POSTGRES_USER,
                                  password=POSTGRES_PASSWORD,
                                  host=POSTGRES_HOST,
                                  port=POSTGRES_PORT,
                                  database=POSTGRES_DBNAME);
    cursor = connection.cursor();

def existUser(chat_id):
    
    #test down
    _exist = False
    #test up
    
    if(_exist):
        return 1;
    else:
        return USER_DOESNT_EXIST

def loadInfo(chat_id):
    return 0;

