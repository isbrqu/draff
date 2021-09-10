# for item in "$folder_output/"*.txt;do
#     while IFS=' ' read -r line;do
#         if [[ -n "$line" && "$line" != *"$TITLE"* ]];then
#             value="${line#*@(:|DNI)}"
#             # trim
#             value="${value##+([[:space:]])}"
#             value="${value%%+([[:space:]])}"
#             row="$row,\"$value\""
#         fi
#         # for field in "${fields[@]}";do
#         #     value="${line#$field}"
#         #     echo "$value"
#         # done
#     done < "$item"
#     echo "$row"
#     break
# done

