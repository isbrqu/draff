[
    .results[0].users[]
    | . + (
        .name
        | ascii_downcase
        # | capture("(?<name>.+\\w)[ (]+((?<dni>\\d+)@|(?<email>[^@]+))";"x")
        | capture("(?<name>.+\\w)[ (]+((?<dni>\\d+)@|(?<email>[^)]+))";"x")
    )
]
| sort_by(.email)
| ["email","dni","name","id"] as $cols
| map(. as $row | $cols | map($row[.])) as $rows
| $cols, $rows[]
| @csv

