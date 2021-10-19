#!/usr/bin/env bash

# Force execution to halt if there are any errors in this script:
set -e
set -o pipefail

../obsidian-repos-downloader.py --help > usage.txt

# TODO Clean out previous downloads before running

mkdir -p downloads-for-docs-ungrouped
pushd    downloads-for-docs-ungrouped
../../obsidian-repos-downloader.py  --limit 4 2>&1 > ../console-output-ungrouped.txt
tree -L 1 -d plugins themes                   2>&1 > ../tree-output-ungrouped.txt
popd

mkdir -p downloads-for-docs-grouped
pushd    downloads-for-docs-grouped
../../obsidian-repos-downloader.py  --limit 4 --group-by-user     2>&1 > ../console-output-grouped.txt
tree -L 2 -d plugins themes                                       2>&1 > ../tree-output-grouped.txt
popd
