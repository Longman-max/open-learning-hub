#!/bin/bash

PROJECT_ROOT=$(dirname $(dirname $(realpath $0)))

echo "Setting up Open Learning Hub..."

required_dirs=(
    "cheat-sheets/languages"
    "cheat-sheets/tools"
    "cheat-sheets/frameworks"
    "programming-languages/python/basics"
    "programming-languages/python/projects"
    "programming-languages/javascript/basics"
    "programming-languages/javascript/projects"
    "programming-languages/typescript/basics"
    "programming-languages/typescript/projects"
    "libraries-and-frameworks/django/mini-projects"
    "libraries-and-frameworks/pandas/examples"
    "topics/data-structures/examples"
    "topics/machine-learning/algorithms"
    "topics/machine-learning/datasets"
    "topics/cyber-security/resources"
    "resources/articles"
    "resources/videos"
    "resources/tutorials"
    "resources/research-papers"
)

for dir in "${required_dirs[@]}"; do
    mkdir -p "$PROJECT_ROOT/$dir"
done

note_files=(
    "programming-languages/python/notes.md"
    "programming-languages/javascript/notes.md"
    "programming-languages/typescript/notes.md"
    "libraries-and-frameworks/django/notes.md"
    "libraries-and-frameworks/pandas/notes.md"
    "topics/data-structures/notes.md"
    "topics/machine-learning/notes.md"
    "topics/cyber-security/notes.md"
)

for note in "${note_files[@]}"; do
    if [ ! -f "$PROJECT_ROOT/$note" ]; then
        echo "# $(basename ${note%.*} | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}g')" > "$PROJECT_ROOT/$note"
        echo -e "\nNotes and documentation for $(basename ${note%.*} | sed 's/-/ /g')" >> "$PROJECT_ROOT/$note"
    fi
done

echo "Setup complete. Project structure initialized."
