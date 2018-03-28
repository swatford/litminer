
# coding: utf-8

# In[ ]:

import pymongo

def mongo_connect(uri="mongodb://swatford:nothing@fe.epa.gov/swatford?authSource=swatford"):
    """uri example: mongodb://{username}:{password}@{host}/{database}?authSource={authenticationDatabase}"""
    return pymongo.MongoClient(uri)

