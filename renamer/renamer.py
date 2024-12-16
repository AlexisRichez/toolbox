import os
import re

def remove_pattern_from_filenames(directory, pattern):
    """
    Preview and optionally rename files in the specified directory by removing the given pattern.

    Args:
        directory (str): Path to the directory containing the files.
        pattern (str): The regex pattern to remove from filenames.

    Returns:
        None
    """
    while True:
        # Compile the regex pattern
        regex = re.compile(pattern)

        files_to_rename = []

        for filename in os.listdir(directory):
            # Ensure we only process files (not directories)
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                # Remove the pattern using regex substitution
                new_filename = regex.sub("", filename).strip()

                # Store the files to rename if the name changed
                if new_filename != filename:
                    files_to_rename.append((filename, new_filename))

        # Preview the changes
        if files_to_rename:
            print("Preview of changes:")
            for original, new in files_to_rename:
                print(f"'{original}' -> '{new}'")

            # Confirm renaming
            confirm = input("Do you want to proceed with renaming? (yes/no): ").strip().lower()
            if confirm == "yes":
                for original, new in files_to_rename:
                    original_path = os.path.join(directory, original)
                    new_path = os.path.join(directory, new)
                    os.rename(original_path, new_path)
                    print(f"Renamed: '{original}' -> '{new}'")
                break
            else:
                print("No files were renamed.")
                # Prompt for a new pattern
                pattern = input("Enter a new pattern to remove (regex supported): ").strip()
        else:
            print("No files matched the pattern or needed renaming.")
            # Prompt for a new pattern
            pattern = input("Enter a new pattern to remove (regex supported): ").strip()

if __name__ == "__main__":
    print("====================================================")
    print("== Basic pattern renamer")
    print("====================================================")
    # Specify the directory and the pattern to remove
    directory_path = input("Enter the directory path: ").strip()

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Display the first 5 files for confirmation
        files_in_directory = os.listdir(directory_path)
        print("First 5 files in the directory:")
        for file in files_in_directory[:5]:
            print(file)

        confirm_directory = input("Is this the correct directory? (yes/no): ").strip().lower()
        if confirm_directory == "yes":
            pattern_to_remove = input("Enter the pattern to remove (regex supported): ").strip()
            remove_pattern_from_filenames(directory_path, pattern_to_remove)
        else:
            print("Directory confirmation failed. Exiting.")
    else:
        print("Invalid directory path.")
