import os
import glob

from config import *


class TrashCleaner:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.folder_tree = []
        self.flagged_files = {}

    def __str__(self):
        return self.target_dir

    def get_folder_tree(self):
        self.folder_tree = [i[0] for i in os.walk(self.target_dir)]
        return self.folder_tree

    def get_flagged_files(self, file_mask=FILE_MASK):
        for folder in self.folder_tree[::-1]:
            self.flagged_files[folder] = glob.glob(f'{folder}/{file_mask}')
        return self.flagged_files

    # def __str__(self):
    #     return self.folder_tree


target_dir = TARGET_DIR
file_mask = FILE_MASK
delete_flag = DELETE_FLAG

tc = TrashCleaner(target_dir)
tc.get_folder_tree()
print(tc.get_flagged_files())
