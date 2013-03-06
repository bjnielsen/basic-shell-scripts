
# awk from field 2 to end of line.
| awk '{$1=""}1'

# awk from field 4 to end of line. EOL. eol.
| awk '{$3=""}1'
