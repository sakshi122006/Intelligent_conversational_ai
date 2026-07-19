import os
from sqlalchemy import create_engine

def get_engine():
    # DATABASE_URL example:
    # mssql+pyodbc://sa:password@mssql:1433/ksppolice?driver=ODBC+Driver+17+for+SQL+Server
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        raise RuntimeError('DATABASE_URL not set')
    engine = create_engine(database_url, fast_executemany=True)
    return engine
