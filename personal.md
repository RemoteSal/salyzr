export OPENAI_API_KEY=your_key
pip install -r requirements.txt

python backend/ingestion/ingest.py
python backend/app.py
streamlit run ui/streamlit_app.py
