from storage import *
from memorystorage import *
from filestorage import *
from jsonstorage import *

storage = StorageProxy()   # in memory
storage.save("Test Data Memory")
print(storage.load())

storage = StorageProxy("file")   # in file
storage.save("Test Data File")
print(storage.load())

storage = StorageProxy("json")   # in json
storage.save(dictionary)
print(storage.load())

