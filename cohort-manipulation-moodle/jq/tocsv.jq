[
    .[]
    | . + (
        .name
        | ascii_downcase
        | capture("(?<name>.+\\w)[ (]+((?<dni>\\d+)@|(?<email>[^@]+))";"x")
        # | capture("(?<name>.+\\w)[ (]+((?<dni>\\d+)@|(?<email>[^)]+))";"x")
    )
]
| ["id","dni","email","name"] as $cols
| map(. as $row | $cols | map($row[.])) as $rows
| $cols, $rows[]
| @csv

