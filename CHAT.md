 To identify and copy only the unique `.txt` files from a super-directory to a subdirectory on macOS, you can use a combination of shell commands such as `find`, `md5sum`, and `cp`. Here’s a step-by-step guide:

1. **Navigate to the Super-Directory**: First, make sure you are in the directory that contains all your `.txt` files.

2. **Generate a List of MD5 Checksums for All `.txt` Files**: Use `find` to locate all `.txt` files and then use `md5sum` to generate checksums for each file.

3. **Sort and Deduplicate the Checksums**: Use a shell command to sort the checksums and remove duplicates.

4. **Copy Unique Files to Subdirectory**: Finally, copy the unique files to your subdirectory.

Here’s how you can do it:

```sh
# Navigate to the super-directory (if not already there)
cd /path/to/super-directory

# Generate a list of md5 checksums for all .txt files and save them in a temporary file
find . -type f -name "*.txt" -exec md5sum {} + > checksum_list.txt

# Sort the checksums and remove duplicates
sort checksum_list.txt | uniq > unique_checksum_list.txt

# Create or navigate to the subdirectory where you want to copy the unique files
mkdir -p /path/to/subdirectory
cd /path/to/subdirectory

# Copy the unique .txt files based on the checksum list
while read -r line; do
    file_path=$(echo "$line" | awk '{print $2}')
    cp -- "$file_path" "../unique_files/"
done < ../unique_checksum_list.txt
```

### Explanation:
1. **`find . -type f -name "*.txt"`**: This command finds all files (`-type f`) with the `.txt` extension in the current directory (`.`) and its subdirectories.
2. **`md5sum {} +`**: For each file found by `find`, this generates an MD5 checksum. The `{} +` syntax allows `find` to pass multiple arguments to `md5sum` at once.
3. **`sort | uniq`**: This sorts the checksums and removes duplicates, leaving only unique checksums.
4. **`while read -r line; do ... done < ../unique_checksum_list.txt`**: This loop reads each line (each unique checksum with its file path) from `unique_checksum_list.txt`, extracts the file path using `awk '{print $2}'`, and then copies the file to the subdirectory.

### Notes:
- Ensure you have execute permissions for all scripts being run (`chmod +x scriptname`).
- Adjust paths as necessary to fit your directory structure.
- This method assumes that filenames do not contain characters that would interfere with shell processing (like spaces or special characters). If there are such characters, additional quoting and escaping may be required.

