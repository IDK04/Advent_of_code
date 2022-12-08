current_dir = []
dirs = {'/': {'files': [],  'total_size': 0}}
dirs_total_size = {}
listing_a_dir = False

def get_nested_folder(dirs, path):
    if len(path) == 0:
        return dirs
    else:
        return get_nested_folder(dirs[path[0]], path[1:])

def add_size(file_size, dirs, path):
    if len(path) == 1:
        dirs['/']['total_size'] += file_size
        dirs_total_size[''.join(path)] = dirs['/']['total_size']
    else:
        current_folder = get_nested_folder(dirs, path)
        current_folder['total_size'] += file_size

        dirs_total_size[''.join(path)] = current_folder['total_size']

        return add_size(file_size, dirs, path[:-1])

with open('input', 'r') as file:
    for line in file.readlines():
        action = line.split()

        if action[0] == '$':
            if action[1] == 'cd':
                if action[2] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(action[2])
            elif action[1] == 'ls':
                listing_a_dir = True
        
        if listing_a_dir:
            if action[0] == 'dir':
                get_nested_folder(dirs, current_dir)[action[1]] = {'files':[], 'total_size': 0}
            try:
                size = int(action[0])
                current_folder = get_nested_folder(dirs, current_dir)
                if 'files' in current_folder.keys():
                    current_folder['files'].append((action[0], action[1]))
                else:
                    current_folder['files'] = (action[0], action[1])
                add_size(size, dirs, current_dir)
            except:
                pass

smallest_dir_to_delete_size = dirs_total_size['/']
unused_space = 70000000 - dirs_total_size['/']
print()

for dir, size in dirs_total_size.items():
    size_needed = abs(unused_space - 30000000)
    if size < smallest_dir_to_delete_size and size > size_needed:
        smallest_dir_to_delete_size = size

print(smallest_dir_to_delete_size)


''' part 1
total_size = 0
for dir, size in dirs_total_size.items():
    if size < 100000:
        total_size += size'''
