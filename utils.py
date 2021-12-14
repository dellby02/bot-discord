from pymongo import MongoClient
import json
from pathlib import Path
import os

cluster = MongoClient(os.environ['mongo'])

economy = cluster["discord"]["economy"]

def inc_bal(bal: int, u):
  member = economy.find_one({"id": u})
  final = member['money'] + bal
  return economy.update_one({"id": u}, {"$set":{"money":final}})

def is_register(u: int):
  return economy.find_one({"id": u})

def rev_bal(rem: int, us):
  member_2 = is_register(us)
  final_2 = member_2['money'] - rem
  return economy.update_one({"id": us}, {"$set": {"money":final_2}})
  
def rev_coin(bal: int, u):
  member = is_register(u)
  check = member['ycoin'] - bal
  economy.update_one({"id": u}, {"$set":{"ycoin":bal}})
  
def check(i):
  conf = Path("./emotes.json")
  with open(conf) as f:
    info = json.load(f)
    return info[i]
    
    
  
