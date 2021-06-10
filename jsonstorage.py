import json
from os import name

dictionary ={
    "name": "json",
    "number": "1111"
}

class JSONStorage:
  def __init__(self):
    self.name = "data.json"
    
  def save(self,data):
    with open (self.name, "w") as j:
      json.dump( data, j )
   
 
  def load(self):
    with open(self.name, 'r') as j:
      data = json.load(j)
      return(data)
 





  