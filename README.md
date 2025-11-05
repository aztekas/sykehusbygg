# Sykehusbygg

PoC/MVP på en RAG for standardromkatalogen mm

## Development

### Setup

1. Install `pipx` 

    On mac:

        brew install pipx
        pipx ensurepath

    On Windows and Linux follow these [instructions](https://pipx.pypa.io/stable/installation/) (scroll down a bit)

    
2. Install uv 
    
    `pipx install uv`

3. Setup virtual environment

    Run this command in your repo root:

    `uv sync`

    This should:

    - Create your virtual environment in `.venv`
    - Install all necessary packages
    - Build the package `sykehusbygg` in editable mode


### Introduction

A short introduction to RAG concepts can be found [here](src/tutorial/README.md)



