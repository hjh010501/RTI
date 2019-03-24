from pymongo import MongoClient
import urllib.parse
from RTI.loader import database_load
import RTI.configs

DB_HOST = urllib.parse.quote_plus(RTI.configs.MONGO_HOST)
DB_TABLE = urllib.parse.quote_plus(RTI.configs.MONGO_TABLE)
DB_NAME = urllib.parse.quote_plus(RTI.configs.MONGO_USER)
DB_PASSWORD = urllib.parse.quote_plus(RTI.configs.MONGO_PASSWORD)

client = MongoClient('mongodb://%s:%s@%s/%s' % (DB_NAME, DB_PASSWORD, DB_HOST, DB_TABLE))
db = client.rti

database_load('battery',
              'cpu',
              'memory',
              'disk')