# Sykehusbygg

PoC/MVP på en RAG for standardromkatalogen mm

## Development

### Environment

1. Install `pipx` 

    On mac:

        brew install pipx
        pipx ensurepath

    On Windows and Linux follow these [instructions](https://pipx.pypa.io/stable/installation/) (scroll down a bit)

    
2. Install uv 
    
    `pipx install uv`

3. Clone this repo and enter the repo folder (root)

4. Setup virtual environment

    Run this command:

    `uv sync`

    This should:

    - Create your virtual environment in `.venv`
    - Install all necessary packages
    - Build the package `sykehusbygg` in editable mode

### Tools

#### Makefile

Run the help command to see available targets
```
make help
```
Alternatively, open [Makefile](Makefile)
### Introduction

A short introduction to RAG concepts can be found [here](src/tutorial/README.md)



