import codecs
import os

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned = ''
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
            continue
        elif char == '>':
            inside_tag = False
            continue
        if not inside_tag:
            cleaned += char

    lines = cleaned.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write('\n'.join(non_empty_lines))

input_path = r'E:\PycharmProjects\PythonProject1\.venv\dz_12_1\draft.html'
output_path = r'E:\PycharmProjects\PythonProject1\.venv\dz_12_1\cleaned.txt'

delete_html_tags(input_path, output_path)
