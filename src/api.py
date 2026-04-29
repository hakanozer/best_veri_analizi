from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.service import load_data, guc_1000_max_12000, tum_data_sayfalama

app = FastAPI()
# cors http://localhost:5173/ ile frontend bağlantısı için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

df = load_data()

# uvicorn src.api:app --reload
@app.get("/guc1000")
def ozet():
    return guc_1000_max_12000(df).to_dict(orient="records")

# ?page=1&size=10
@app.get("/tum_data")
def tum_data(page: int = 1, size: int = 10):
    return tum_data_sayfalama(df, page=page, size=size)