from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware  # if using CORS
from fastapi.responses import JSONResponse
import os
import shutil
from app.parser import parse_document

app = FastAPI()

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/parse-pdf")
async def parse_pdf(
    file: UploadFile = File(...),
    password: str = Form(...)
):
    
       # Define save path
    save_path = f"uploads/{file.filename}"
    
    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)
    
    # Save the uploaded file
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    print(f"File saved at: {save_path}")
    
    # Pass the file path to parse_document
    result = parse_document(save_path, password)
    
    return JSONResponse(content=result, status_code=200)