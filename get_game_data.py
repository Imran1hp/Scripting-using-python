import os
import json
import shutil
from subprocess import PIPE,run
import sys

GAME_DIR_PATTERN = "game"



def find_all_game_paths(source):
     game_paths =[]

     for root,dirs,files in os.walk(source):
          for directory in dirs:
               if GAME_DIR_PATTERN in directory.lower():
                    path =os.path.join(source,directory)
                    game_paths.append(path)
          break
          
     return game_paths

def get_name_from_paths(paths,to_strip):
     new_name =[]
     for path in paths:
          _,dir_name = os.path.split(path)
          new_dir_name = dir_name.replace(to_strip,"")
          new_name.append(new_dir_name)
     return new_name



def create_dir(path):
     if not os.path.exists(path):
          os.mkdir(path)   


def copy_and_overwrite (source,dest):
     if os.path.exists(dest):
        shutil.rmtree(dest)
     shutil.copytree(source,dest)


def main (source,target):
     cwd= os.getcwd()
     source_path = os.path.join(cwd,source)
     target_path = os.path.join(cwd,target)
     game_paths = find_all_game_paths(source_path)
     new_game_dirs = get_name_from_paths(game_paths,"game")
     
     create_dir(target_path)

     for src,dest in zip(game_paths,new_game_dirs):
          dest_path = os.path.join(target_path,dest)
          copy_and_overwrite(src,dest_path)
     
     
     print(new_game_dirs)

if __name__ == "__main__":
     args = sys.argv
     if len(args)!=3:
          print("You must pass a source directory and a target directory -only.")
     source,target = args[1:]    
     main(source,target) 






