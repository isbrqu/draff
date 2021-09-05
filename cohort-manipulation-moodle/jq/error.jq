if (has("error")) then
    .error
elif (.results | length == 0) then
    "user not found"
elif (.results[0].users | length == 0) then
    .results[0].name
else
    ""
end
