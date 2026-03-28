import os
from sqlalchemy import create_engine, text

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DB_URL, pool_pre_ping=True)

async def query(sql, params=None): # parameterized queries
    if params is None:
        params = {}

    with engine.connect() as connection:
        res = await connection.execute(text(sql), params)
        connection.commit()

        if res.returns_rows:
            return [dict(row._mapping) for row in res]
        
        return {"inserted_id": res.lastrowid, "affected_rows": res.rowcount}