import os
from fastapi import FastAPI, UploadFile,HTTPException
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from inference_gfpgan import inference_main
from utils import clean_directory,get_filename_from_path

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



upload_folder = "results/cmp"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
upload_folder = "results/cropped_faces"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
upload_folder = "results/restored_faces"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
upload_folder = "results/restored_imgs"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

upload_folder = "inputs/whole_imgs"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)




@app.post("/upload_file/")
async def create_upload_file(file: UploadFile):
    """
    Function allow upload image to specific route
    """
    if file.content_type not in ["image/jpeg"] and file.content_type not in ["image/png"]:
        raise HTTPException(400, detail="Invalid document type, the format correct is .JPG,.JPEG or PNG")
    file_name = os.path.join(upload_folder, file.filename)
    # Save the uploaded image to the specified folder
    # clean previus image preprocesing
    clean_directory('inputs/whole_imgs')
    clean_directory('results/cmp')
    clean_directory('results/cropped_faces')
    clean_directory('results/restored_faces')
    clean_directory('results/restored_imgs')
    
    with open(file_name, "wb") as f:
        f.write(file.file.read())
    result_dimesion_image=inference_main(file.filename)
    return result_dimesion_image


@app.get("/get_image")
async def main():
    """
    function to get the image from specific folder where the image was processed: the path is results/restored_imgs
    """
    filename_image_to_restore=get_filename_from_path('results/restored_imgs')
    some_file_path = f'{os.getcwd()}/results/restored_imgs/{filename_image_to_restore}'
    return FileResponse(some_file_path)