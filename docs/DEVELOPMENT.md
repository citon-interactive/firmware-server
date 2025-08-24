# Development

This document outlines the development process for this project, including setup instructions, coding standards, and contribution guidelines.

## Getting Started

Make a venv:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install build
pip install -e .
```
Build the package:

```bash
python -m build
```

run the package:

```bash
python -m main
```