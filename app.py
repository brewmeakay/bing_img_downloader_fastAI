#https://pypi.org/project/bing-image-downloader/
#pip install bing-image-downloader


from bing_image_downloader import downloader
import os, shutil
from pathlib import Path

dataset_name='bears'
path=Path(dataset_name)

#creates the parent dataset folder
if not path.exists():
    path.mkdir()

labels=['grizzly', 'brown', 'teddy']

for l in labels:
    downloader.download(query=f'{l} bear',limit=200,output_dir=path,adult_filter_off=True)

    #changes the folder name from default to fastAI label specific
    if not Path(f"{path}/{l}").exists():
        os.rename(f"{path}/{l} bear", f"{path}/{l}")

    #add code to handle folder management if code is run multiple times 




    
