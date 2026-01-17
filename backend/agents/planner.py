import traceback
from typing import List,Any,Callable,Dict

class Planner:

    def __init__(self):
        pass


    def _create_plan(self,query:str) -> dict:

        query = query.lower()
        print("--debug create_plan----", query)

        if "policy" in query or "compliance" in query:
            return {"scope": "documents", "k": 8}

        if "ticket" in query or "issue" in query:
            return {"scope": "jira", "k": 5}

        return {"scope": "all", "k": 6}


