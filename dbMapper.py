import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from defines import *

CONNECTION = 0;
CURSOR = 0;

def connectDB():
    global CONNECTION
    global CURSOR

    CONNECTION = psycopg2.connect(user=POSTGRES_USER,
                                  password=POSTGRES_PASSWORD,
                                  host=POSTGRES_HOST,
                                  port=POSTGRES_PORT,
                                  database=POSTGRES_DBNAME);
    CURSOR = CONNECTION.cursor();

def selectQuery(arg_tablename, arg_fields, arg_termField, arg_termValue):
    global CURSOR

    _queryText = "SELECT ";
    _queryText += arg_fields;
    _queryText += " FROM ";
    _queryText += arg_tablename;
    _queryText += " WHERE ";
    _queryText += arg_termField;
    _queryText += " = ";
    _queryText += arg_termValue;
    _queryText += ";";

    print(_queryText);

    CURSOR.execute(_queryText);
    # Получить результат
    _fetchResult = CURSOR.fetchone();

    print(_fetchResult);

    return _fetchResult;

def deleteQuery(arg_tablename, arg_termField, arg_termValue):
    global CURSOR
    #пока лень писать, позже 


def updateQuery(arg_tablename, arg_termField, arg_termValue):
    global CURSOR
    #аргументы будут другие. поля и значения добавить. но скорее всего универсальной функции просто не будет
    #пока лень писать, позже 

def complexQuery(arg_query_text):
    global CURSOR

    CURSOR.execute(arg_query_text);
    _fetchResult = CURSOR.fetchone();

    return _fetchResult;