import argparse
from pathlib import Path 
parser=argparse.ArgumentParser('add eding for send in email')
parser.add_argument('command',type=str,help='prepare to send parse to change back')
parser.add_argument('path',type=str,help='path to prepare')
parser.add_argument('--extesions','-e',type=str, nargs='+',help ='file to parse')


args=parser.parse_args()

path_to_change=Path(args.path)

for file_change in path_to_change.rglob('*'):
    if file_change.is_file():
        if args.command=='prepare':
             for ext in args.extesions :
                 if file_change.suffix == ext:
                    new_file_name = file_change.with_suffix(file_change.suffix + '.temp')
                    file_change.rename(new_file_name)
        elif args.command == 'parse':
               if file_change.suffix == '.temp':
                    new_file_name = file_change.with_name(file_change.name[:5])
                    file_change.rename(new_file_name)
               