import os
import glob

from config import *


class TrashCleaner:

    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.flagged_files = {}
        self.all_files = {}

    def __str__(self):
        return self.target_dir

    def get_folder_tree(self):
        self.folder_tree = [i[0] for i in os.walk(self.target_dir)]
        return self.folder_tree

    def get_all_files(self, file_mask=FILE_MASK):
        self.get_folder_tree()
        for folder in self.folder_tree[::-1]:
            self.all_files[folder] = glob.glob(f'{folder}/{file_mask}')
        return self.all_files

    # def process(self):
    #     self.get_folder_tree()
    #     self.get_all_files(file_mask='*.*')
    #     self.get_all_files(file_mask=file_mask)


target_dir = TARGET_DIR
file_mask = FILE_MASK
delete_flag = DELETE_FLAG

tc = TrashCleaner(target_dir)
# # tc.get_folder_tree()
# # tc.get_all_files(file_mask='*.*')
# tc.get_all_files(file_mask=file_mask)

print(tc.get_all_files(file_mask='*.*'))
print(tc.get_all_files(file_mask=file_mask))
