# 1C_functions_parsing
Here I'm parsing 1C language functions and procedures and extracting information from comments on them using ANTRL4.

## Usage
**compile_grammar.sh** - rebuilds the Python parser module for grammar from files with .g4 extensions  
**clear.sh** - cleans up files

File with **antrl.ipynb** extension contains code, that parses example module and produces Pandas DataFrame with code, comment_text and data extracted from comments.

## Note
Rebuilds Python modules with grammar parsers from files with the extension '.g4'. Makes fixes necessary for the parsers to work.
