from pathlib import Path

#Find  all the csv files that contain 'search_text'
# Below are the folder path
folder = Path('2022-csv-renamed')
search_text = '202201'

# this is the glob function 
for path in folder.glob('**/*.csv'):
    # print(path)
    if search_text in path.name: 
        print(path)
        print(path.absolute())
