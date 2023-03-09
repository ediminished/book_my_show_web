from .db_models import TestTable
from .db_engine import DBEngine


class DAO:
    @classmethod
    def get_test_data(cls):
        with DBEngine.get_db_session() as session:
            rows = session.query(TestTable).all()
            if rows:
                for row in rows:
                    print(row.id, row.age)
