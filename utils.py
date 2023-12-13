import os
import shutil



def clean_directory(path_image:str)->None:
    """
    Description: Function to clean files of previus inference. 
    Input: string like path_image
    Output:None
    The files is stored in the following folders:
    - inputs/whole_imgs
    - results/cmp
    - results/cropped_faces
    - results/restored_faces
    - results/restored_imgs
    """
    file_list = os.listdir(path_image)
    for file_name in file_list:
        file_path = os.path.join(path_image, file_name)
        try:
            os.remove(file_path)
            print(f"Removed {file_name}")
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")




def clean_previus_predictions(folder_path):
    items = os.listdir(folder_path)
    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            try:
                shutil.rmtree(item_path)
                print(f"Removed directory: {item}")
            except Exception as e:
                print(f"Error deleting directory {item}: {e}")




def get_filename_from_path(path_image:str)->str:
    """
    Description: Function to get the name of image to show in front
    Input: the name of the image
    Output:name of the image like a string
    """
    file_list = os.listdir(path_image)
    try:
        return file_list[0]
    except Exception as e:
        print(f"erro in get image : {e}")