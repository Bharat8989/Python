from pathlib import Path


# List Files and Folders
def readfileandfolder():
    path = Path(".")

    items = list(path.iterdir())

    print("\n===== FILES & FOLDERS =====")

    if len(items) == 0:
        print("No files or folders found.")
        return

    for i, item in enumerate(items, start=1):
        if item.is_file():
            print(f"{i}. 📄 {item.name}")
        else:
            print(f"{i}. 📁 {item.name}")


# Create File
def createfile():
    try:
        name = input("Enter file name: ")

        with open(name, "x") as fs:
            data = input("Enter data: ")
            fs.write(data)

        print("✅ File created successfully")

    except FileExistsError:
        print("❌ File already exists")

    except Exception as err:
        print(f"Error: {err}")


# Read File
def readfile():
    try:
        name = input("Enter file name to read: ")

        with open(name, "r") as fs:
            data = fs.read()

        print("\n===== FILE CONTENT =====")
        print(data)

    except FileNotFoundError:
        print("❌ File not found")

    except Exception as err:
        print(f"Error: {err}")


# Update File
def updatefile():
    try:
        name = input("Enter file name to update: ")

        with open(name, "a") as fs:
            data = input("Enter new data: ")
            fs.write("\n" + data)

        print("✅ File updated successfully")

    except FileNotFoundError:
        print("❌ File not found")

    except Exception as err:
        print(f"Error: {err}")


# Delete File
def deletefile():
    try:
        name = input("Enter file name to delete: ")

        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("✅ File deleted successfully")
        else:
            print("❌ File not found")

    except Exception as err:
        print(f"Error: {err}")


# Main Menu
while True:

    print("\n========================")
    print("      FILE MANAGER")
    print("========================")
    print("1. Create File")
    print("2. Read File")
    print("3. Update File")
    print("4. Delete File")
    print("5. List Files & Folders")
    print("6. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            createfile()

        elif choice == 2:
            readfile()

        elif choice == 3:
            updatefile()

        elif choice == 4:
            deletefile()

        elif choice == 5:
            readfileandfolder()

        elif choice == 6:
            print("🙏 Thank You!")
            break

        else:
            print("❌ Invalid Choice")

    except ValueError:
        print("❌ Please enter a valid number")