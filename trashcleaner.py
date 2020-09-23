import os
import glob

from config import *


def get_files(folder, file_mask):
    """
    Get files from the folder
    :param folder: path to folder (absolute)
    :param file_mask: file mask (*.ext)
    :return: files list
    """

    return glob.glob(f'{folder}/{file_mask}')


def get_folder_tree(target_dir):
    """
    Get the tree list from absolute path to target directory
    :param target_dir: absolute path to target directory
    :return: folder tree list
    """

    return [i[0] for i in os.walk(target_dir)]


def trash_cleaner(target_dir, delete_flag=False):

    # Get folder tree list
    folder_tree = get_folder_tree(target_dir=target_dir)

    files = []
    flagged_files = []

    for folder in folder_tree[::-1]:

        print(f'\nFound in "{folder}":')

        # Get all files from current folder
        files = get_files(folder=folder, file_mask='*.*')
        print(f'Total file(s): {len(files)}')

        # Get all flagged (*.bak) files from current folder
        flagged_files = get_files(folder=folder, file_mask=FILE_MASK)
        print(f'{FILE_MASK} file(s): {len(flagged_files)}')

        for file in flagged_files:

            # Check if the parent file exist
            parent_file = get_files(folder=folder, file_mask=os.path.basename(file).split('.')[0] + '.*')

            # Delete child file
            if len(parent_file) == 1:
                os.remove(file)
                print(f'Delete file "{os.path.basename(file)}" - OK!')

        # Check if current folder is empty
        files = get_files(folder=folder, file_mask='*.*')

        # Delete empty folder
        if delete_flag:
            if len(files) == 0 and get_folder_tree(target_dir=folder)[-1] == folder:
                os.rmdir(folder)
                print(f'Empty folder "{folder}". Delete - OK!')


print(f'Destination folder: {TARGET_DIR}')

trash_cleaner(target_dir=TARGET_DIR, delete_flag=DELETE_FLAG)
