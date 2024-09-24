
from fastapi import FastAPI,Form 
from fastapi.middleware.cors import CORSMiddleware 

from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add")
def add_num(a: int=Form(...), b: int=Form(...)):
    return{"sum": a + b}
    
    
    

    
    