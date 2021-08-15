# poetry-template

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/gabrielguarisa/poetry-template/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/gabrielguarisa/poetry-template/releases)
[![License](https://img.shields.io/github/license/gabrielguarisa/poetry-template)](https://github.com/gabrielguarisa/poetry-template/blob/master/LICENSE)

A python project template using poetry and with a few useful features

</div>

## Usage

First, install cookiecutter using pip:

```bash
$ pip install cookiecutter
```

Then, to create a new project, run:

```bash
$ cookiecutter gh:gabrielguarisa/poetry-template
```

### Variables

- `project_name`: The name of the project.
- `project_description`: A short description of the project.
- `version`: The version of the project.
- `author`: The name of the author.
- `email`: The email of the author.
- `github_name`: The author Github username.
- `license`: The license of the project.
- `minimal_python_version`: The minimal Python version required.
- `line_length`: The line length of the project.

## Features

- [poetry](https://python-poetry.org/)
- [pytest](https://docs.pytest.org/en/latest/) and [pytest-cov](https://pypi.org/project/pytest-cov/)
- [black](https://github.com/psf/black)
- [pre-commit](https://pre-commit.com/)
- [isort](https://github.com/PyCQA/isort)
- [pyupgrade](https://github.com/asottile/pyupgrade)

## Setting up a development environment

If you don't have a local development environment, you can follow these steps to set one up.

First, if you have not already, install [poetry](https://python-poetry.org/):

```bash
pip install poetry
```

Now, initialize poetry and [pre-commit](https://pre-commit.com/) hooks:

```bash
make install && make install-pre-commit
```

### Running the tests

You can run the tests with:

```bash
make test
```

This will run the tests with [pytest](https://docs.pytest.org/en/latest/) and show information about the coverage.

### Formatting the code

To format the code, you can use the command:

```bash
make formatting
```

This will run the [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort) and )[pyupgrade](https://github.com/asottile/pyupgrade) commands.

If you want to just check the formatting, use the command:

```bash
make check-formatting
```

### Releasing a new version

To release a new version, you need to follow these steps:

1. Update the version with `poetry version <version>` and commit the changes. This project follows [Semantic Versioning](http://semver.org/), so the version number should follow the format `<major>.<minor>.<patch>`. Alternatively, you can also use the version as `major` or `minor` or `patch`, and the version number will be automatically incremented.

2. Create a Github release with the new version number.

3. (Optional) Publish the new version to PyPI with `poetry publish --build`.


## Credits

Some projects that inspired this repo:

- [Python Packages Project Generator](https://github.com/TezRomacH/python-package-template)
- [Jace's Python Template](https://github.com/jacebrowning/template-python)
- [cookiecutter-python](https://github.com/timothycrosley/cookiecutter-python)
- [Cookiecutter PyPackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
- [Python Project Wizard](https://github.com/zillionare/cookiecutter-pypackage)