from azure.core.exceptions import ResourceExistsError
from azure.data.tables import TableServiceClient

from Backend.CloudStorage.ITableStorage.i_ride_info_table_storage import IRideInfoTableStorage

TABLE_NAME = "RidesInfo"
AZURE_TABLE_CONNECTION = "UseDevelopmentStorage=true"
class RideInfoTableStorage(IRideInfoTableStorage):

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
            print('An error was occurred during creating or updating RideInfo : ', e)

    def get_all(self):
        try:
            return self.table_client.query_entities(query_filter=None)
        except Exception as e:
            print('An error was occurred while fetching data from RidesInfo cloud table storage ', e)

    def get_by_id(self, row_key):
        try:
            return self.table_client.get_entity(partition_key="rideinfo", row_key = row_key)
        except Exception as e:
            print('An error was occurred while fetching data for rideInfo by ID : ', e)

    def get_by_user_id(self, user_row_key):
        try:
            results = list(self.table_client.query_entities(query_filter=None))
            ride_info = [x for x in results if x["UserId"] == user_row_key]
            return  ride_info[0]
        except Exception as e:
            print('An error was occurred while fetching data for rideInfo by UserID : ', e)


    def delete_by_id(self, row_key):
        try:
            return self.table_client.delete_entity(partition_key="rideinfo", row_key=row_key)
        except Exception as e:
            print('An error was occurred while trying to delete the RidInfo ', e)
