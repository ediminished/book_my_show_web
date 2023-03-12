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
        return [{"id": 1, "age": 18}, {"id": 5, "age": 34}]

    @classmethod
    def add_row_to_test_data(cls):
        data = {"id": 8, "age": 33}
        with DBEngine.get_db_session() as session:
            session.add(TestTable(**data))
