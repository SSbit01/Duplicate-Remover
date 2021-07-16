from os import *
from filecmp import *

all_files = sorted(listdir())

this_file = path.basename(__file__)
all_files.remove(this_file)

dont_delete = [this_file]

for i in all_files:
  duplicate = False
  for j in dont_delete:
    if cmp(i,j):
      duplicate = True
      break
  if not duplicate:
    dont_delete.append(i)

delete_files = list(set(all_files) - set(dont_delete))
length = len(delete_files)

if length == 0:
  print("No duplicate files")
elif length == 1:
  print("Duplicate file: "+delete_files[0]+"\nAre you sure to delete it?")
else:
  print("Duplicate files: "+"".join(delete_files)+"\nAre you sure to delete them?")

system("pause")

for i in delete_files:
  remove(i)