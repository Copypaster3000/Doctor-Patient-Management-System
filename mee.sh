while read -r line; do
    file_path=$(echo "$line" | awk '{print $2}')
    cp -- "$file_path" "../unique_files/"
done < ../unique_checksum_list.txt
