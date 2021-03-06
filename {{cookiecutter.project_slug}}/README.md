# {{ cookiecutter.project_slug }}

[![image-size]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }}. "More on itisfoundation/{{ cookiecutter.project_slug }}.:staging-latest image")

[![image-badge]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")
[![image-version]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")
[![image-commit]](https://microbadger.com/images/itisfoundation/{{ cookiecutter.project_slug }} "More on {{ cookiecutter.project_name }} image in registry")

{{ cookiecutter.project_short_description }}

<!-- Add badges urls here-->
[image-size]:https://img.shields.io/microbadger/image-size/itisfoundation/{{ cookiecutter.project_slug }}./staging-latest.svg?label={{ cookiecutter.project_slug }}.&style=flat
[image-badge]:https://images.microbadger.com/badges/image/itisfoundation/{{ cookiecutter.project_slug }}.svg
[image-version]https://images.microbadger.com/badges/version/itisfoundation/{{ cookiecutter.project_slug }}.svg
[image-commit]:https://images.microbadger.com/badges/commit/itisfoundation/{{ cookiecutter.project_slug }}.svg
<!------------------------->

## Development

```console
make help
```

Standard dev workflow is

```console
make venv
source .venv/bin/activate

(.venv) make requirements
(.venv) make install

(.venv) make test
```

To start the service just check (some config files under ``{{cookiecutter.project_slug}}/src/{{cookiecutter.package_name}}/config`` )

```console
{{ cookiecutter.command_line_interface_bin_name }} --help

{{ cookiecutter.command_line_interface_bin_name }} --config config-host-dev.yml
```
