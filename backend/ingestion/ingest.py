import os
from store.vector_store import add_documents


class Ingestor:
    def __init__(self,texts:list,meta:list):
        self.texts = texts
        self.meta = meta

    def ingest_docs(self):
        texts = self.texts
        meta = self.meta

        for file in os.listdir("data/docs"):
            with open(f"data/docs/{file}") as f:
                content = f.read()
                texts.append(content)
                meta.append({"source": file})

        add_documents(texts, meta)

    
if __name__ == "__main__":
    ingestor = Ingestor()
    result = ingestor.ingest_docs()

    print("--debug ingestor res-----", result)
