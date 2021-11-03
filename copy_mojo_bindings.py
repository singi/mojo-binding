#! /usr/bin/python

import os
import shutil
import sys

base_path = sys.argv[1]
for path, dirs, files in os.walk(base_path):
  for file in files:
    if file == 'mojo_bindings.js' or file == 'mojo_bindings_lite.js':
      shutil.copyfile(os.path.join(path, file), os.path.join('./', file))
    
    if file.endswith('.mojom.js') or file.endswith('.mojom-lite.js') or file.endswith('.mojom.m.js'):
      target_path = os.path.join('./', path[len(base_path) + 1:])
      try:
        os.makedirs(target_path)
      except:
        pass
      shutil.copyfile(os.path.join(path, file), os.path.join(target_path, file))
