#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create a text file with specified content

version_added: "1.0.0"

description:
  - Creates or updates a UTF-8 text file.
  - Does not change the file when its content already matches.

options:
  path:
    description: Path to the text file. The parent directory must exist.
    required: true
    type: path
  content:
    description: Text to write to the file.
    required: true
    type: str

author:
  - Eugenie Kotukov (@beeasierbebetter)
'''

EXAMPLES = r'''
- name: Create a text file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_own_module.txt
    content: "Hello from Ansible!\n"
'''

RETURN = r'''
path:
  description: Path to the managed text file.
  type: str
  returned: success
  sample: /tmp/my_own_module.txt
'''

import os
import tempfile

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    result['path'] = path
    content = module.params['content'].encode('utf-8')

    try:
        current = None
        if os.path.exists(path):
            with open(path, 'rb') as existing_file:
                current = existing_file.read()

        result['changed'] = current != content

        if module.check_mode:
            module.exit_json(**result)

        if result['changed']:
            descriptor, temporary_path = tempfile.mkstemp(dir=module.tmpdir)
            module.add_cleanup_file(temporary_path)

            with os.fdopen(descriptor, 'wb') as temporary_file:
                temporary_file.write(content)

            module.atomic_move(temporary_path, path)

    except OSError as error:
        module.fail_json(msg='Cannot manage file: %s' % error, **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
