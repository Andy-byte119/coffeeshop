from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATBASE_URL = 'mysql+mysqlconnector://Coffee_Admin:New_Coffee_Password_1234@localhost/CoffeeShopNew'
engine = create_engine(DATBASE_URL, echo=True)
Base = declarative_base()
Sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
#решить проблему актуальности sqlalchemy

#создание таблиц
class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key = True)
    title = Column(String(30), nullable = False)
    photo = Column(String(200), nullable = False)
    price = Column(Integer, nullable = False)

class FranchiseRequest(Base):
    __tablename__ = "franchise_request"

    id = Column(Integer, primary_key = True)
    full_name = Column(String(30), nullable = False)
    phone = Column(String(15), nullable = False)
    email = Column(String(100), nullable = False)

Base.metadata.create_all(engine)
print("Таблицы созданы")

def get_db():
    db = Sessionlocal()
    try:
        return db
    except Exception:
        db.close()
        raise