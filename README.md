# obsidian-community-repositories-downloader

<!-- toc -->
## Contents

  * [Usage](#usage)
  * [Maintenance notes](#maintenance-notes)
    * [Automated updating the table of contents](#automated-updating-the-table-of-contents)
    * [Almost-automated updating of usage](#almost-automated-updating-of-usage)<!-- endToc -->

Download every approved Obsidian.md community Plugin and Theme - to read and search the source code and learn from the
community.

[![on-push-do-doco](https://github.com/claremacrae/obsidian-community-repositories-downloader/actions/workflows/updateMarkdown.yml/badge.svg)](https://github.com/claremacrae/obsidian-community-repositories-downloader/actions/workflows/updateMarkdown.yml)

## Usage

<!-- snippet: usage.txt -->
<a id='snippet-usage.txt'></a>
```txt
usage: obsidian-community-repos-downloader.py [-h] [-o OUTPUT_DIRECTORY]

Clone repos included in the obsidian-releases repo, to provide a body of
example plugins and CSS themes.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        The directory where repos will be downloaded. Must
                        already exist. Defaults to the current working
                        directory.
```
<sup><a href='/tests/usage.txt#L1-L11' title='Snippet source file'>snippet source</a> | <a href='#snippet-usage.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

---

## Maintenance notes

### Automated updating the table of contents

The table of contents is updated automatically by a GitHub Action, on every push to GitHub.

### Almost-automated updating of usage 

The above usage is updated automatically, on push, whenever `tests/usage.txt` is changed.

To update `tests/usage.txt:

```bash
# 1. Update tests/usage.txt
cd tests
./update_usage.sh
# 2. Commit update usage.txt
# 3. Push to github - a GitHub Action will then update the usage text in this README
```
