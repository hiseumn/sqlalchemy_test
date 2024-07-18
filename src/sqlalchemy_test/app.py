import csv
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy_test.infra.models.memo import Memo


#.envファイルからpostgreSQLのユーザー名とパスワードを取得
username=os.getenv("SQL_USERNAME")
password=os.getenv("SQL_PASSWORD")

# db作成
engine=create_engine(f"postgresql+psycopg://postgres:postgres@localhost:5432/memo")
Session = sessionmaker(bind=engine)
session = Session()


#csvファイルからデータを読み込み、postgreSQLにデータを挿入
with open("test_data.csv","r",encoding="utf-8") as csvfile:
    reader=csv.reader(csvfile)
    next(reader) #csvファイルの1行目(列名)を除く
    for row in reader:
        memo=Memo(id=row[0],memo=row[1])
        session.add(memo)
    session.commit()
