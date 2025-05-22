from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getEconomicData")
def get_economic_data(pais: str, evento: str):
    return {
        "pais": pais,
        "evento": evento,
        "resultado": "3.6%",
        "esperado": "3.4%",
        "anterior": "3.2%",
        "data_evento": "2025-05-21 10:30"
    }