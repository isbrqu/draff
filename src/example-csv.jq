regex='(?<name>.+\\w)[ (]+((?<dni>\\d+)@|(?<email>[^)]+))'
tocsv='(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv'
tocsv='["id","dni","email","name"] as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv'
echo "$json" | jq -r '[ .results[0].users[] | . + ( .name | ascii_downcase | capture("'"$regex"'";"x")) ]'" | $tocsv"
# in file
[
    .results[0].users[]
    | . + (
        .name
        | ascii_downcase
        | capture("(?<name>.+\\w)[ (]+((?<dni>\\d+)@|(?<email>[^)]+))";"x")
    )
]
| ["id","dni","email","name"] as $cols
| map(. as $row | $cols | map($row[.])) as $rows
| $cols, $rows[]
| @csv

