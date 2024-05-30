
# foo_param Documentation

## Introduction

Welcome to the foo_param Documentation  . This document provides information for the project.

## Dependencies

1. python 3.12.3:

```sh
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
pyenv global 3.12.3
```

2. pytest 8.2.1:

```sh
python -m pip install -U pytest
```