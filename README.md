# Open Learning Hub

A comprehensive collection of programming resources, documentation, and learning materials organized for easy access and learning.

## Repository Structure

```
OPEN-LEARNING-HUB/
│
├── cheat-sheets/                    # Quick reference PDFs and guides
│   ├── languages/                   # Programming language cheat sheets
│   ├── tools/                       # Development tools quick references
│   └── frameworks/                  # Framework and library cheat sheets
│
├── programming-languages/           # Language-specific learning folders
│   ├── python/
│   │   ├── basics/                 # Core concepts and fundamentals
│   │   ├── projects/               # Practice projects and examples
│   │   └── notes.md               # General documentation
│   ├── javascript/
│   └── typescript/
│
├── libraries-and-frameworks/        # Frameworks and libraries
│   ├── django/
│   │   ├── mini-projects/         # Small practice projects
│   │   └── notes.md              # Framework documentation
│   └── pandas/
│       ├── examples/              # Data analysis examples
│       └── notes.md              # Library documentation
│
├── topics/                         # General CS and tech concepts
│   ├── data-structures/
│   │   ├── examples/             # Implementation examples
│   │   └── notes.md             # Concept explanations
│   ├── machine-learning/
│   │   ├── algorithms/          # ML algorithm implementations
│   │   ├── datasets/           # Sample datasets for practice
│   │   └── notes.md           # Topic documentation
│   └── cyber-security/
│
├── resources/                      # General learning materials
│   ├── articles/                  # Saved articles and blog posts
│   ├── videos/                    # Video tutorial links
│   ├── tutorials/                 # Step-by-step guides
│   └── research-papers/          # Academic papers and publications
│
└── tools/                         # Project utilities and scripts
    ├── setup.sh                   # Environment setup script
    └── organize.py               # Project organization helper
```

## Usage

### Getting Started
1. Clone this repository
2. Browse the folders based on your learning goals
3. Follow the folder structure when adding new content

### Project Scripts
The `tools` directory contains utility scripts that should only be run in specific situations:

- `setup.sh`: Run ONLY when:
  - Setting up a fresh clone of the repository
  - Initializing a new section that's missing required directories
  - Recovering from corrupted or deleted directory structure

- `organize.py`: Run ONLY when:
  - Performing bulk reorganization of files
  - Cleaning up misplaced files across directories
  - Moving multiple files to their correct locations

⚠️ DO NOT run these scripts during normal usage as they may reorganize your existing file structure.

### Contributing
1. Follow the existing folder structure
2. Add meaningful documentation in notes.md files
3. Keep PDFs and resources organized in appropriate directories
4. Update this README when adding new sections

For small changes:
- Manually place files in their correct directories
- Create new subdirectories as needed
- Update relevant notes.md files

For large reorganizations:
1. Back up your changes
2. Use `organize.py` to help with bulk file movements
3. Review the changes to ensure correct organization
