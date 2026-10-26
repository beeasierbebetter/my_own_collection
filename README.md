# my_own_namespace.yandex_cloud_elk

This collection contains the `my_own_module` module and the `my_own_role` role, which uses the module to create a text file

## Environment

- Ansible Core 2.16.3
- Python 3.12

## Module: my_own_module

Creates or updates a UTF-8 text file on the managed host \
The parent directory must already exist

| Parameter | Type | Required | Description |
|---|---|---|---|
| path | path | Yes | Path to the text file |
| content | str | Yes | Content to write to the file |

The module returns `changed: false` when the existing content matches \
Check mode is supported

Example task:

```yaml
- name: Create a text file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/example.txt
    content: "Hello from Ansible!\n"
```

The returned `path` field contains the path to the managed file

## Role: my_own_role

The role contains a single task that calls the collection module

| Variable | Default | Description |
|---|---|---|
| my_own_role_path | /tmp/my_own_collection.txt | Value passed to path |
| my_own_role_content | Hello from my own collection!\n | Value passed to content |

Default values are defined in `roles/my_own_role/defaults/main.yml`

See `playbook.yml` for an example of using the role \
Connection settings are defined in `inventory.yml`

## Build

Run from the collection root directory:

```bash
ansible-galaxy collection build
```

## Installation and execution

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
ansible-playbook -i inventory.yml playbook.yml
```

## Author

Eugenie Kotukov

The module retains the original template's copyright notice:
Copyright (c) 2018, Terry Jones.

## License

GPL-3.0-or-later
