# How this process works

1. read folders from `data/input`
2. read files from each folder
3. for each file:
    - ignore files that don't have a `.html` extension
    - read file content
    - turn file content into markdown using `markdownify`
    - check if `data/output/<folder_name>` exists, if not, create it
    - save markdown file to `data/output/<folder_name>/<file_name>.md`
