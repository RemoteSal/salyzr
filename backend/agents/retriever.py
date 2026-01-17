import time
import re
from backend.store.vector_store import search, enhanced_search


class Retreiver:

    def __init__(self):
        pass


    def _retrieve(self,query:str,plan:dict):
    
        # results = search(query, plan["k"])
        results = enhanced_search(query, plan["k"])
        return results


