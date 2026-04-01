import os
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(DB_URL, pool_pre_ping=True)

async def query(sql, params=None): # parameterized queries
    if params is None:
        params = {}

    async with engine.connect() as connection:
        res = await connection.execute(text(sql), params)

        if res.returns_rows:
            return [dict(row._mapping) for row in res]
        
        return {"inserted_id": res.lastrowid, "affected_rows": res.rowcount}