import os
import warnings
from backend.store.vector_store import add_documents


warnings.filterwarnings("ignore", category=RuntimeWarning)


class Ingestor:
    def __init__(self, texts: list, meta: list):
        self.texts = texts
        self.meta = meta

    def ingest_docs(self):
        for file in os.listdir("data/docs"):
            file_path = os.path.join("data/docs", file)

            with open(file_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()

            self.texts.append(content)
            self.meta.append({"source": file})

        add_documents(self.texts, self.meta)


if __name__ == "__main__":
    ingestor = Ingestor(texts=[], meta=[])
    ingestor.ingest_docs()
    print("\n\nIngestion completed successfully", ingestor.meta, ingestor.texts)
