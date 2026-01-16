import time
import re
from store.vector_store import search


class Retreiver:

    def __init__(self):
        pass


    def _retrieve(self,query:str,plan:dict):
    
        results = search(query, plan["k"])
        return results


