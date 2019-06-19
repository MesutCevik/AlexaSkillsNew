import os
import glob


# metadata_files = [f for f in glob.glob("*.json")]

os.chdir('./new_metadata')

metadata_files = [f for f in glob.glob("*.json")]

print(metadata_files)
