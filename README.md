# immo_eliza_deployment

   - API that runs a program predicting real estate prices in Belgium
   - pip install -r requirements.txt or docker build -t immo_eliza .
   - uvicorn app:app --reload or docker run -p 8000:8000 -it immo_eliza