export OPENAI_API_KEY=your_key
pip install -r requirements.txt

python backend/ingestion/ingest.py
python backend/app.py
streamlit run ui/streamlit_app.py


Initially ingestion and serving were separate processes, so the vector index wasn’t shared. For the MVP, I load documents at backend startup to guarantee deterministic availability. In production, this would move to persistent storage.
