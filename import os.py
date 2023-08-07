import os
import argparse

def rename_files(directory_path, prefix=''):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Loop through each file and rename it
    for index, filename in enumerate(files):
        # Construct the new file name with the specified prefix and index
        new_name = f"{prefix}{index + 1}_{filename}"

        # Get the absolute paths of the old and new file names
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_name)

        try:
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description='Rename files in a directory.')
    parser.add_argument('directory_path', help='Path to the directory containing the files')
    parser.add_argument('--prefix', default='', help='Prefix for the new file names (optional)')
    args = parser.parse_args()

    # Call the function with the provided directory path and prefix
    rename_files(args.directory_path, args.prefix)
