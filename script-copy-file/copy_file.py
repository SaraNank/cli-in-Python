import argparse
import shutil
from pathlib import Path
parser=argparse.ArgumentParser('Copys a given file to another location')
parser.add_argument('old',type=str,help='old file to copy')
parser.add_argument('stem',type=str,help='ending file to copy')
parser.add_argument('new',type=str,help='new path for the file')

args=parser.parse_args()
old_path=Path(args.old)
for file in old_path.rglob(f'*.{args.stem}'):
    if file.is_file():
        shutil.copy(file, args.new)
