from pathlib import Path
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# create file1, ..., file9 (.txt)
for i in numbers:
    with open(f'test{i}.txt', 'w') as file:
        file.write('Testing this')

# delete all txt files
for path in Path('.').glob('*.txt'):
    print(path)
    path.unlink()

# delete all but test9.txt
for path in Path('.').glob('test[1-8].txt'):
    print(path)
    path.unlink()

