from pathlib import Path
import zipfile

current_directory = Path('.')
# This is just the destination directory. it will create that directory
target_directory = Path('temp')

for path in current_directory.glob('*.zip'):
    print(path)
    # This is just using the zipfile library. extract all inside path
    with zipfile.ZipFile(path, 'r') as zip_obj:
        zip_obj.extractall(path=target_directory)
