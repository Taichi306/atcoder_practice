import os
import glob

crr_dir_path = "/home/hoge/public"
img_file_path = []

def dfs(crr_dir_path):
    for node in glob.glob(crr_dir_path + "/*"):
        if os.path.isfile(node) and check_img(node):
            img_file_path.append(node)
        elif os.path.isdir(node):
            dfs(node)

dfs(crr_dir_path)



def check_img():
    return 
    