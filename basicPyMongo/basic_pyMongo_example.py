#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, get, request, abort
import datetime
from pymongo import MongoClient

# Connect To DB
try:
  connection = MongoClient('localhost',27017)
except:
  print("Could Not Connect to Mongo DB")
  
db = connection['market']
collection = db['stocks']

##########
# Create #
##########
@route('/createStock', method='POST')
def create_stock():
  """ 
      # createStock
      *Route /createStock, method POST*
      ### Required Felids
      **Ticker**: Three letter stock ticker identifer\n
      **Price**: floating point value stock price
      ### Return
      On failed insert: 400\n
      On failed connection: 404\n
      Success: json, {"_id"}
      ### Example
      ```curl -H "Content-Type: application/json" -X POST -d'{"Ticker":"ZZZ","Price":5}' http://localhost:8000/createStock```
   """
  try:
    result = ""
    data = request.json
    if data:
      try:
        result = collection.save(data)
      except:
        abort(400)
  except:
    abort(404)
  return json.loads(json.dumps(result, indent=4, default=json_util.default)) 

########
# Read #
########
@route('/getStock', method='GET')
def get_stock():
  """ 
  # getStock
  *Route /getStock, method GET*
  ### Required Felids
  **Ticker**: Three letter stock ticker identifer
  ### Return
  On failed retreval or bad formating: 400\n
  On failed connection: 404\n
  On Success: json, {"Price", "_id", "Ticker"}
  ### Example
  ```curl http://localhost:8080/getStock?Ticker="ZZZ"```
  """
  try:
    result = ""
    request.query.Ticker
    ticker = request.query.Ticker
    query = {"Ticker": ticker}
    if ticker:
      try:
        result = collection.find_one(query)
      except:
        abort(400)
  except NameError:
    abort(404)
  if result:
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
  else:
    return "Nothing Found\n"
    
##########
# Update #
##########

@route('/updatePrice', method='POST')
def update_price():
  """ 
  # updatePrice
  *Route /updatePrice, method POST*
  ### Required Felids
  **Ticker**: Three letter stock ticker identifer\n
  **Price**: floating point value stock price
  ### Return
  On failed retreval or bad formating: 400\n
  On failed connection: 404\n
  On Success: json {"Price","_id","Ticker"}
  ### Example
  ```curl -H "Content-Type: application/json" -X POST -d'{"Ticker":"ZZZ","Price":15}' http://localhost:8000/updatePrice```
  """
  try:
    response = ""
    data = request.json
    
    if data:
      query = {"Ticker": data['Ticker']}
      document = { "$set" : {"Price": data['Price']} }
    else:
      abort(400)
    # This could be much cleaner
    if query and document:
      try:
        response = collection.find_one_and_update(query, document)
      except:
        abort(400)
    else:
      print("missing id or data...")
  except:
    abort(404)
  if response:  
    #Figure out how to get a newline at the end of this, super ugly in console
    return json.loads(json.dumps(response, indent=4, default=json_util.default))
  else:
    abort(500)

###########
# DESTROY #
###########
@route('/delete', method='GET')
def delete():
  """ 
  # delete
  *Route /delete, method GET*
  ### Required Felids
  **Ticker**: Three letter stock ticker identifer
  ### Return
  On failed deletion or bad formating: 400\n
  On failed connection: 404\n
  On Success: json, {"_id"}
  ### Example
  ```curl http://localhost:8080/delete?Ticker="ZZZ"```
  """
  try:
    response = ""
    request.query.Ticker
    ticker = request.query.Ticker
    if ticker:
      query = {"Ticker":ticker}
      try:
        response = collection.delete_one(query)
      except:
        abort(400)
  except:
    abort(404)
  return "Deleted %s\n"%(id)

###########
# Summary #
###########
@route('/getSummary', method='POST')
def get_summary():
  """ 
  # getSummary
  *Route /getSummary, method POST*
  ### Required Felids
  **list**: json formatted list of Tickers\n
  ### Return
  On failed retreval: 500\n
  On failed connection: 404\n
  On Success: json {{"Price","_id","Ticker"},{"Price","_id","Ticker"},etc for length of list}
  ### Example
  ```curl -H "Content-Type: application/json" -X POST -d'{"list":{"AAA","BBB","CCC"}}' http://localhost:8000/getSummary```
  """
  try:
    response = []
    data = request.json
    list = data['list']
   
    if list:
      for i in list:
        try:
          print(i)
          response.append(collection.find_one({"Ticker":i},{"Ticker":1, "Price":1}))
        except:
          abort(500)
  except:
    abort(404)
  
  return json.dumps(response, indent=4, default=json_util.default)

#########
# Top 5 #
#########
@route('/topFive', method='GET')
def top_five():
  """ 
  # topFive
  *Route /getSummary, method POST*
  ### Required Felids
  **industry**: name of an industry
  ### Return
  On failed retreval: 500\n
  On failed connection: 404\n
  On Success: json {{"Price","_id","Ticker"},{"Price","_id","Ticker"},etc for length of list}
  ### Example
  ```curl http://localhost:8080/topfive?industry="Medical%20Laboratories%20%26%20Research"```
  """
  try:
    request.query.Industry
    industry = request.query.Industry
    #industry = "Medical Laboratories & Research"
    pipeline = [
      {"$match":{"Industry":industry}},
      {"$sort":{"Price":-1}},
      {"$limit": 5},
      {"$group": {"_id": "$Ticker", "Price":{"$sum":"$Price"}}} #had to sum price to make the group work, should be ok, not sure why it wants to be this way
    ]
    if industry:
      try:
        response = collection.aggregate(pipeline)
      except:
        abort(500)
  except:
    abort(404)
  
  # gotta json it line by line, not sure why
  final = []
  for i in response:
    print(i)
    final.append(json.dumps(i, indent=4, default=json_util.default))
  return final
###############
# Main Method #
###############
if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  
  
