from azure.core.exceptions import ResourceExistsError
from azure.data.tables import TableServiceClient
from Backend.CloudStorage.ITableStorage.i_taxi_license_table_storage import ITaxiLicenseTableStorage

TABLE_NAME = "Licenses"
AZURE_TABLE_CONNECTION = "UseDevelopmentStorage=true"
class TaxiLicenseTableStorage(ITaxiLicenseTableStorage):



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
            print('An error was occurred during creating or updating license : ', e)

    def get_all(self):
        try:
            return self.table_client.query_entities(query_filter=None)
        except Exception as e:
            print('An error was occurred while fetching data from licenses cloud table storage ', e)

    def get_by_id(self, row_key):
        try:
            return self.table_client.get_entity(partition_key="license", row_key = row_key)
        except Exception as e:
            print('An error was occurred while fetching data for license by ID : ', e)

    def get_by_user_id(self, row_key) -> bool:
        try:


            results = list(self.table_client.query_entities(query_filter=None))
            license_exist = [x for x in results if x["UserId"] == row_key]

            if license_exist:
                return True
            else:
                return False
        except Exception as e:
            print("An error was occurred while trying to get license by user_id", e)
    def delete_by_id(self, row_key):
        try:
            return self.table_client.delete_entity(partition_key="license", row_key=row_key)
        except Exception as e:
            print('An error was occurred while trying to delete the license ', e)
