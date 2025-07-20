import os
import json
import shutil
from subprocess import PIPE,run
import sys


def main (source,target):
     cwd= os.getcwd()
     source = os.path.join(cwd,source)
     target = os.path.join(cwd,target)

if __name__ == "__main__":
     args = sys.argv
     if len(args)!=3:
          print("You must pass a source directory and a target directory -only.")


     source,target = args[1:]    
     main(source,target) 






