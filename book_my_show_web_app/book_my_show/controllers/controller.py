from db.dao import DAO


class BookMyShow:
    @staticmethod
    def get_users():
        users = DAO.get_test_data()
        return {"users": users, "success": True}
