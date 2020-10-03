import os
import glob

from config import *


class TrashCleaner:

    file_mask = FILE_MASK

    def __init__(self, target_dir=TARGET_DIR):

        self.target_dir = target_dir
        self.all_files = {}
        self.flagged_files = {}
        self.parent_file = None

    def __str__(self):
        return self.target_dir

    def get_folder_tree(self):
        self.folder_tree = [i[0] for i in os.walk(self.target_dir)]
        return self.folder_tree

    def get_all_files(self, file_mask='*.*'):
        self.get_folder_tree()

        for folder in self.folder_tree[::-1]:
            self.all_files[folder] = glob.glob(f'{folder}/{file_mask}')

        print(self.all_files)
        return self.all_files

    def get_flagged_files(self, file_mask=file_mask):
        self.get_folder_tree()

        for folder in self.folder_tree[::-1]:
            self.flagged_files[folder] = glob.glob(f'{folder}/{file_mask}')

        return self.flagged_files

    def remove_trash_files(self, file_mask=file_mask):
        # self.get_folder_tree()
        self.get_all_files()
        self.get_flagged_files()

        for flagged, parent in zip(self.flagged_files.values(), self.all_files.values()):
            print(f'flagged = {len(flagged)}\nparent = {len(parent)}')
            if flagged == parent:
                print('ok\n')
                continue
            print('not ok\n')
            for file in flagged:
                print(parent.findall(file))
                if file.split('.')[0] in [parent_file.split('.')[0] for parent_file in parent]:
                    print('Delete', file)
