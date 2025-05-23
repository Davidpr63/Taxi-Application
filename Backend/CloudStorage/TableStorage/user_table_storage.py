from azure.core.exceptions import ResourceExistsError

from Backend.CloudStorage.ITableStorage.i_user_table_storage import IUserTableStorage
from azure.data.tables import TableServiceClient

TABLE_NAME = "Users"
AZURE_TABLE_CONNECTION = "UseDevelopmentStorage=true"
class UserTableStorage(IUserTableStorage):

    def __init__(self):
        self.table_service = TableServiceClient.from_connection_string(conn_str=AZURE_TABLE_CONNECTION)
        self.table_client = self.table_service.get_table_client(TABLE_NAME)
        try:
            self.table_service.create_table(table_name=TABLE_NAME)
        except ResourceExistsError:
            pass

        self.table_client = self.table_service.get_table_client(table_name=TABLE_NAME)

    def create_or_update(self, entity):
        try:
            print(entity)
            self.table_client.upsert_entity(entity)
        except Exception as e:
            print('An error was occurred during creating or updating user : ', e)

    def get_all(self):
        try:
            return self.table_client.query_entities(query_filter=None)
        except Exception as e:
            print('An error was occurred while fetching data from user cloud table storage ', e)

    def get_by_id(self, row_key):
        try:
            return self.table_client.get_entity(partition_key="user", row_key = row_key)
        except Exception as e:
            print('An error was occurred while fetching data for user by ID : ', e)

    def get_by_username(self, username) -> bool:
        try:
            filter_query = f"Username eq '{username}'"

            results = list(self.table_client.query_entities(query_filter=None))
            user = [x for x in results if x["Username"] == username]

            if user is None:
                return None
            else:
                return user


        except Exception as e:
            print('An error was occurred while fetching data for user by Username:  ', e)
    def delete_by_id(self, row_key):
        try:
            return self.table_client.delete_entity(partition_key="user", row_key=row_key)
        except Exception as e:
            print('An error was occurred while trying to delete the user ', e)
