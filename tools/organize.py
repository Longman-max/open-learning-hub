#!/usr/bin/env python3
import os
import shutil
import re
from pathlib import Path

def organize_files(root_dir):
    root = Path(root_dir)
    
    patterns = {
        r'.*\.(pdf|PDF)$': {
            'cheat': 'cheat-sheets',
            'python|javascript|typescript|julia': 'cheat-sheets/languages',
            'vim|keyboard|markdown': 'cheat-sheets/tools',
            'django|pandas|scikit': 'cheat-sheets/frameworks'
        },
        r'.*\.(md|MD)$': {
            'python': 'programming-languages/python',
            'javascript': 'programming-languages/javascript',
            'typescript': 'programming-languages/typescript',
            'django': 'libraries-and-frameworks/django',
            'pandas': 'libraries-and-frameworks/pandas',
            'data.?structures': 'topics/data-structures',
            'machine.?learning': 'topics/machine-learning',
            'security': 'topics/cyber-security'
        }
    }

    for file_path in root.rglob('*'):
        if file_path.is_file():
            for pattern, rules in patterns.items():
                if re.match(pattern, file_path.name):
                    for keyword, dest_dir in rules.items():
                        if re.search(keyword, file_path.name, re.I):
                            dest_path = root / dest_dir / file_path.name
                            if not dest_path.exists():
                                dest_path.parent.mkdir(parents=True, exist_ok=True)
                                shutil.move(str(file_path), str(dest_path))
                                print(f"Moved {file_path.name} to {dest_dir}")

def clean_empty_dirs(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            dir_to_check = os.path.join(dirpath, dirname)
            if not os.listdir(dir_to_check):
                os.rmdir(dir_to_check)
                print(f"Removed empty directory: {dirname}")

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print("Organizing files...")
    organize_files(root_dir)
    print("Cleaning empty directories...")
    clean_empty_dirs(root_dir)
    print("Organization complete!")
