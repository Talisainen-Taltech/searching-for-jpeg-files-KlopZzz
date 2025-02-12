import os
import requests
import zipfile


folder = "random_files"


r = requests.get("https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip")
with open("random_files_without_extension.zip", "wb") as file:
    file.write(r.content)


with zipfile.ZipFile("random_files_without_extension.zip", "r") as zip_ref:
    zip_ref.extractall()

# Kas kaust eksisteerib
if os.path.exists(os.path.join("random_files", "random_files")):
    #Loob Path
    extract_folder = os.path.join("random_files", "random_files")


for name in os.listdir(folder):
    fp = os.path.join(folder, name)

    if os.path.isdir(fp):
        continue

    with open(fp, "rb") as f:
        signature = f.read(2)

    #Kontrollib kas fail on pilt
    if s == b"\xff\xd8":
        new_path = fp + ".jpeg"
        os.rename(fp, new_path)
    else:
        os.remove(fp)

os.remove("random_files_without_extension.zip")