import os
import shutil


def copyfile_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file_name in os.listdir(source_dir):
        from_path = os.path.join(source_dir, file_name)
        dest_path = os.path.join(dest_dir, file_name)
        print(f"{from_path} --> {dest_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copyfile_recursive(from_path, dest_path)
