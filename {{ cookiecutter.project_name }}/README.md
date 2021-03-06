# {{ cookiecutter.project_name }}

<div align="center">

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)

{{ cookiecutter.project_description }}

</div>

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

