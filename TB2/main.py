from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import uvicorn
from app.buku import Buku
from app.database import create_table, post_buku, get_buku
from app.logger import logger
from app.exceptions import HTTPException500

app = FastAPI()

class BukuRequest(BaseModel):
    judul: str
    penulis: str
    penerbit: str
    tahun_terbit: int
    konten: str
    iktisar: str

@app.post("/buku")
async def add_buku(request: Request, buku_request: BukuRequest):
    try:
        # Logging request body
        logger.info(f"Request Body: {await request.json()}")
        
        buku = Buku(
            buku_request.judul,
            buku_request.penulis,
            buku_request.penerbit,
            buku_request.tahun_terbit,
            buku_request.konten.split(","),
            buku_request.iktisar
        )
        post_buku(buku)
        return {"message": "Buku berhasil ditambahkan"}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException500(detail=str(e))

@app.get("/buku/{judul}")
def read_buku(judul: str):
    try:
        buku = get_buku(judul)
        if buku is None:
            raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
        return buku
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException500(detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
