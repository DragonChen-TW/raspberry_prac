from pymongo import MongoClient
import datetime
import Adafruit_DHT
from bson.objectid import ObjectId
from bson.son import SON
from pprint import pprint

def insert_data(temperature, humidity, datetime):
    post = {
        'location': 'home',
        'temperature': temperature,
        'humidity': humidity,
        'data': datetime.datetime.now()
    }
    post_id = collection.insert_one(post).inserted_id
    print(post_id)
    return post_id

def query_data(id=None):
    for post in collection.find():
        print(post)

def aggregate_data():
    pipeline = [{
        '$sort': SON([("_id", -1)])
    }]
    pprint(list(db.temp_hum_collection.aggregate(pippipeline)))

def del_data(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    return result

if __name__ == '__main__':
    try:
        sensor = Adafruit_DHT.DHT11
        sensor_num = 2
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_num)

        client = MongoClient('localhost', 27017)

        db = client['temp_hum_database']
        collection = db['temp_hum_collection']

        aggregate_data()

    finally:
        pass
