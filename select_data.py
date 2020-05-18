# randomly select 2000 dogs and 2000 cats from kaggle data
# place them in directory structure expected by keras tutorial

import glob
import random
import shutil

source_dir = "./dogs-vs-cats/train"

dogs = random.sample(glob.glob(f"{source_dir}/dog*"),2000)
cats = random.sample(glob.glob(f"{source_dir}/cat*"),2000)

# train
for i,dog in enumerate(dogs[:1000]):
   shutil.copyfile(f"{dog}",f"./data/train/dogs/dog{i:03}.jpg")
for i,cat in enumerate(cats[:1000]):
   shutil.copyfile(f"{cat}",f"./data/train/cats/cat{i:03}.jpg")

# validate
for i,dog in enumerate(dogs[1000:]):
   shutil.copyfile(f"{dog}",f"./data/validation/dogs/dog{i:03}.jpg")
for i,cat in enumerate(cats[1000:]):
   shutil.copyfile(f"{cat}",f"./data/validation/cats/cat{i:03}.jpg")
   
