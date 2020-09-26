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

        # for folder, flagged_files in self.flagged_files.items():
        #     print(f'\nflagged files = {flagged_files}')
        #     for flagged_file in flagged_files:
        #         # print(f'flagged file = {flagged_file}')
        #         if flagged_file in self.all_files[folder] and flagged_file in self.flagged_files[folder]:
        #             print(f'flagged file = {flagged_file}')
        #     parent_files = self.all_files[folder]
        #     print('parent files =', parent_files)

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
            # print(type(flagged), len(flagged), flagged)
            # print(type(parent), len(parent), parent)
            # parent_file = []
            # for file in parent:
            #     parent_file = os.path.basename(file).split('.')[0]
            #     print(f'{parent_file} = {file}')
            #     if parent_file == file:
            #         print('Double')
            #
            # print(flagged)
            # print(parent)
        #     if flagged != parent:
        #         print('ok')
        # for folder, files in self.flagged_files.items():
        #     print(folder)
        #     for file in files:
        #         flagged_file = os.path.basename(file)
        #         print(flagged_file)
        #         parent_file = os.path.basename(flagged_file).split('.')[0] + '.*'
        #         print(parent_file)
        #         if parent_file == flagged_file.split('.')[0] + '.*':
        #             print('OK')

            # if self.parent_files[folder] == 1:
            #     os.remove(file)
            #     print(f'Delete file "{os.path.basename(file)}" - OK!')

    # def process(self):
    #     self.get_folder_tree()
    #     self.get_all_files(file_mask='*.*')
    #     self.get_all_files(file_mask=file_mask)


target_dir = TARGET_DIR
# file_mask = FILE_MASK
delete_flag = DELETE_FLAG

tc = TrashCleaner(target_dir)
# print(tc.get_folder_tree())

# print(tc.get_all_files())
# print(tc.get_all_files(file_mask=file_mask))
# tc.get_flagged_files()
tc.remove_trash_files()
