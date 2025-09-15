import sqlalchemy

class Sql_connection:
    def __init__(self):
        engine = None
    
    def postgres_connect(self, postgresql_user: str
                       , postgresql_password: str,
                        host: str,
                        port: str,
                        database: str ):
        connection_request = f'postgresql+psycopg2://{postgresql_user}:{postgresql_password}@{host}:{port}/{database}'
        self.engine = sqlalchemy.create_engine(connection_request)
        try:
            with self.engine.connect() as connection:
                print('Successfully connected to the PostgreSQL database')
        except Exception as ex:
            print(f'failed to connect to postgreql due to this {ex}')
