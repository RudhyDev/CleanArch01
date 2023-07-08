from .users_repository import UsersRepository


def test_insert_user():
    mocked_first_name = 'valid_name'
    mocked_last_name = 'valid_last_name'
    mocked_age = 18

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
