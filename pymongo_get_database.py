from dotenv import load_dotenv
from pymongo import MongoClient
import os

def configure():
    print('test')


def get_database():
   load_dotenv()
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = f"mongodb+srv://{os.getenv('USERNAME')}:{os.getenv('API_SECRET')}@cluster0.f4werh5.mongodb.net/?retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)

   # Create the database for our example (we will use the same database throughout the tutorial
   return client['GUI_App']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
   # Get the database
   dbname = get_database()