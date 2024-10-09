def remove_duplicates_from_large_file(input_file_path, output_file_path):
    seen = set()
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line not in seen:
                outfile.write(line)
                seen.add(line)

if __name__ == "__main__":
    files = r"C:\Users\v-zhazhai\Desktop\filenames.txt"

    output = r"C:\Users\v-zhazhai\Desktop\filenames_clean.txt"
    remove_duplicates_from_large_file(files,output)