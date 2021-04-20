from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

class AnimalShelter(object):

   def _init_(self, username, password): #Specifies which database to use and authorizes the user
       self.client = MongoClient('mongodb://%s:%s@localhost:36653/test?authSource=AAC' % (username, password))
       self.database = self.client['AAC']

     
   def create(self, data): #Creates a new animal document
       if data is not None: #Inserts document if it exists
           insert = self.database.animals.insert(data)
           if insert != 0:
               return True
           else: 
               return False
       else:
           raise Exception('Nothing to save, because data parameter is empty') #Throws exception if document does not exist
            
   def read(self, data): #Reads an animal document
        #if data is not None: 
            animal = self.database.animals.find(data, {"_id": False}) #Reads document if it exists
            return animal
       # else:
           # raise Exception("Document not specified") #Throws exception if document does not exists       
            
   def update(self, animal, data): #Updates an animal document
       if data is not None:
            result = self.database.animals.update(animal, data) #Updates database if it exists
            result = json.dumps(result) #Converts results to json format
            return result
       else:
            raise Exception("Document not specified") #Throws exception if document does not exists  
   
   def delete(self, animal):
       if animal is not None:
            deleted_animal = self.database.animals.remove(animal) #Removes document if it exists
            deleted_animal = json.dumps(deleted_animal) #Converts results to json format
            return deleted_animal   
       else:
           raise Exception(deleted_animal) #Throws exception if document does not exists  