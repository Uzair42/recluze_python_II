# **Shell Utilities**

The `shutil` module (short for **Shell Utilities**) is a standard Python library used for high-level file operations. While the `os` module is great for interacting with the operating system (like changing directories or checking if a file exists), `shutil` is the "heavy lifter" for moving, copying, and archiving files and folders.

---

##  Why is `shutil` Useful?

In basic Python, opening and writing to a file is easy, but what if you want to copy an entire folder containing 1,000 files? Doing that with basic file commands would require a complex loop.

**`shutil` provides "one-liners" for:**

* **Copying** files and entire directory trees.
* **Moving** files and folders to different locations.
* **Deleting** non-empty folders (which `os.rmdir` cannot do).
* **Archiving** (creating `.zip` or `.tar` files) and extracting them.

---

##  Key Functions at a Glance

| Function | What it does | Best Use Case |
| --- | --- | --- |
| **`shutil.copy(src, dst)`** | Copies a file's content and permissions. | General file copying. |
| **`shutil.copy2(src, dst)`** | Copies file + **metadata** (timestamps). | Backups where dates matter. |
| **`shutil.copytree(src, dst)`** | Copies an **entire folder** recursively. | Cloning a project folder. |
| **`shutil.move(src, dst)`** | Moves or renames a file/folder. | Organizing files. |
| **`shutil.rmtree(path)`** | Deletes an **entire folder** and its contents. | Cleaning up temp directories. |
| **`shutil.make_archive()`** | Compresses a folder into a `.zip` or `.tar`. | Creating backups/shipments. |

---

##  Code Examples

### 1. Copying Files (The "Safe" Way)

When copying, `copy2` is often preferred because it preserves the "Last Modified" and "Created" dates.

```python
import shutil

source = "my_script.py"
destination = "backup/my_script_v2.py"

# This copies the file and keeps the original timestamps
shutil.copy2(source, destination)
print("File copied successfully with metadata!")

```

### 2. Deleting a Folder with Contents

The standard `os.rmdir()` only works if a folder is empty. `shutil.rmtree()` is the "nuclear option"—it deletes everything inside.

```python
import shutil
import os

folder_path = "old_logs"

if os.path.exists(folder_path):
    # DANGER: This deletes the folder and everything inside it!
    shutil.rmtree(folder_path)
    print(f"Successfully deleted {folder_path}")

```

### 3. Creating a Zip Archive

This is incredibly useful for taking a folder full of data and turning it into a single shareable file.

```python
import shutil

# name of the zip file to create, the format, and the folder to zip
shutil.make_archive("project_backup", "zip", "my_project_folder")

print("Zip file created!")

```

### 4. Checking Disk Space

A hidden gem in `shutil` is the ability to check how much space you have left on your hard drive.

```python
import shutil

# Get disk usage for the root directory
total, used, free = shutil.disk_usage("/")

print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

```

---

##  When to use `os` vs `shutil`?

* Use **`os`** when you need to talk to the system: *What is my current directory? Does this file exist? Create a single empty folder.*
* Use **`shutil`** when you need to manipulate files: *Copy this here, move that there, zip this folder, or delete this whole directory tree.*

> **Important Note:** Be very careful with `shutil.rmtree()`. There is no "Undo" or "Recycle Bin" for this command. Once it runs, the data is gone!
