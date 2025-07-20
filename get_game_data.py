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

def create_dir(path):
     if not os.path.exists(path):
          os.mkdir(path)    


def main (source,target):
     cwd= os.getcwd()
     source = os.path.join(cwd,source)
     target = os.path.join(cwd,target)
     game_paths = find_all_game_paths(source)
     create_dir(target)

if __name__ == "__main__":
     args = sys.argv
     if len(args)!=3:
          print("You must pass a source directory and a target directory -only.")


     source,target = args[1:]    
     main(source,target) 






