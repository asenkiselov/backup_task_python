
#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os
import re

def gen(namedir):
  dirlen = []
  for root, dirs, files in os.walk(namedir, topdown=False):
    for name in dirs:
      dirlen.append(os.path.join(root, name))
  return dirlen

def sync(ndir):
  src = ndir
  #searching directory and replace with backup directory
  dest = re.sub("(/prod)", r"\1"+"_backup", src)
  print("Copying date from {} to {}".format(src, dest))
  subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
  d = gen("/home/directory/example/prod")
  p = Pool(len(d))
  p.map(sync,d)
