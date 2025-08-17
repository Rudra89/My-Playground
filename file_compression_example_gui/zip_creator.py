import zipfile
import pathlib

def make_archive(filepaths, folder):
    folder_path = pathlib.Path(folder, 'compressed.zip')
    with zipfile.ZipFile(folder_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)