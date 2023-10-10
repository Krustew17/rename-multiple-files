import os

DIRECTORY = r'C:\Users\GamePC\Desktop\secret\random'

LOOKING_FOR = input(f'What are you looking for: ')
CHANGE_FOR = input(f'What do you want to change it for: ')

AMOUNT_RENAMED_FILES = 0


def get_files(dir):
    return os.listdir(dir)


def get_next_name(file):
    next_name = file.replace(LOOKING_FOR, CHANGE_FOR)
    return next_name


def rename_file(current_name, next_name, file):
    if LOOKING_FOR in file:
        os.rename(fr'{DIRECTORY}\{current_name}',
                  fr'{DIRECTORY}\{next_name}')
        return True
    return False


files = get_files(DIRECTORY)
for file in files:
    next_name = get_next_name(file)
    if rename_file(file, next_name, file):
        AMOUNT_RENAMED_FILES += 1

if AMOUNT_RENAMED_FILES >= 1:
    print(f'Successfully renamed {AMOUNT_RENAMED_FILES} files.')
