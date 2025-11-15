import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# get per file it via parameters
@app.get("/get-pdf/")
async def get_pdf(filename: str):
    # Define the path to your folder
    folder_path = ''
    file_path = os.path.join(folder_path, filename)

    # Check if file exists
    if os.path.exists(file_path):
        return FileResponse(path=file_path, media_type='application/pdf', filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found.")

# Test this via request not in parameters
class PDFRequest(BaseModel):
    pdfName: str

@app.get("/get-pdf2/")
async def get_pdf(pdf_request: PDFRequest):
    # Retrieve the filename from the request body
    filename = pdf_request.pdfName

    # Define the path to your folder
    folder_path = ''
    file_path = os.path.join(folder_path, filename)

    # Check if file exists
    if os.path.exists(file_path):
        return FileResponse(path=file_path, media_type='application/pdf', filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found.")
