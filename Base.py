from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
from mysql.connector import Error

DATBASE_URI = 'mysql+mysqlconnector://username:password@localhost/'
engine = create_engine(DATBASE_URI)
metadata = MetaData()
Base = declarative_base()

Session = sessionmaker(bind = engine)
session = Session()

#создание таблиц
class Menu(Base):
    __tablename__ = "Меню"

    id = Column(Integer, primary_key = True)
    title = Column(String(30), nullable = False)
    price = Column(Integer, nullable = False)

class FranchiseRequest(Base):
    __tablename__ = "Заявления на оформление франшизы"

    id = Column(Integer, primary_key = True)
    full_name = Column(String(30), nullable = False)
    phone = Column(String(15), nullable = False)
    email = Column(String(100), nullable = False)

def create_databases():
    databases = ["Заявления на оформление франшиз", "Меню"]
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "username",
            password = "password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            for db_name in databases:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"База данных '{db_name}' уже существует")
    except Error as e:
        print("Ошибка {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Соединение с MySQl завершено")

def create_tables():
    db_engine = create_engine('')    
