import os 
import shutil 

dst_path = "./public/"
src_path = "./static/"
shutil.rmtree(os.path.normpath(dst_path))
shutil.copytree(os.path.normpath(src_path), os.path.normpath(dst_path))
