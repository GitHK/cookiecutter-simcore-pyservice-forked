# -*- coding: utf-8 -*-
import os
import re


def fix_template_expansion(content, replacements):
    """
    fix template expansion after hook copy
    :param content: the duplicated hook content
    :param replacements: array of dictionaries
                         cookiecutter_key => template key expanded
    """
    for replacement in replacements:
        for key, to_be_replaced in replacement.items():
            replacement = chr(123) + chr(123) + \
                'cookiecutter.' + key + chr(125) + chr(125)
            content = content.replace(to_be_replaced, replacement)
    return content


def get_file_content(file):
    """
    get the content of a given file
    :param file: the file to get the content of
    """
    content = ''
    with open(file, 'r') as f:
        content= f.read()
    return content


def set_file_content(file, content):
    """
    write content to file
    :param file: the file to rewrite its content
    :param content: content to write to the given file
    """
    nchar_written = 0
    with open(file, 'w') as f:
        nchar_written = f.write(content)
    return nchar_written


# format title of the generated readme file
readme = os.getcwd() + '/README.md'
if (os.path.exists(readme)):
    title_underliner = ''.center(len('{{cookiecutter.project_name}}'), '=')
    set_file_content(
        readme,
        re.sub(
            r'^=+$', title_underliner, get_file_content(readme), 1, flags=re.M
        )
    )
# end format title of the generated readme file
