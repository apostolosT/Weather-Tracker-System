from pymongo import MongoClient


retrieve_id = {'_id': False}

class Mongo:
    def __init__(self,uri):
        """
        Set the db reference
        """
        self.connection= MongoClient(uri)
       
    def insert_city(self,db_name,col,args):
        return self.connection[db_name][col].insert_one({"_id":args['city']})

    # def insert_citys(self, db_name, col, citys):
    #     return self.connection[db_name][col].insert_many(citys)

    def find_cities(self,db_name,col):
        cities=self.connection[db_name][col].find()
        # print(f"cities: {[city['_id'] for city in cities]}")
        cities=[city['_id'] for city in cities]
        return ({"cities":cities})

    def find_city(self, db_name, col, args):
        return self.connection[db_name][col].find_one(args['city'], retrieve_id)


    def delete_city(self, db_name, col, city):
        x=self.connection[db_name][col].find_one_and_delete({"_id": city})
        return x


    def drop_col(self, db_name, col):
        return self.connection[db_name][col].drop()