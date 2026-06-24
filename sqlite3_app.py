import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

conn.commit()


def list_videos():
    cursor.execute("SELECT * FROM videos")

    videos = cursor.fetchall()

    if not videos:
        print("\nNo videos found.")
        return

    print("\nVideos:")
    for row in videos:
        print(row)


def add_video(name, time):
    cursor.execute(
        "INSERT INTO videos (name, time) VALUES (?, ?)",
        (name, time)
    )
    conn.commit()
    print("✅ Video Added Successfully")


def update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name=?, time=? WHERE id=?",
        (new_name, new_time, video_id)
    )
    conn.commit()
    print("✅ Video Updated Successfully")


def delete_video(video_id):
    cursor.execute(
        "DELETE FROM videos WHERE id=?",
        (video_id,)
    )
    conn.commit()
    print("✅ Video Deleted Successfully")


def main():

    while True:

        print("\n===== YouTube Manager App =====")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video duration: ")

            add_video(name, time)

        elif choice == '3':

            video_id = int(input("Enter video id: "))
            name = input("Enter new video name: ")
            time = input("Enter new video duration: ")

            update_video(video_id, name, time)

        elif choice == '4':

            video_id = int(input("Enter video id: "))

            delete_video(video_id)

        elif choice == '5':

            print("Thank You!")
            break

        else:
            print("❌ Invalid Choice")

    conn.close()


if __name__ == "__main__":
    main()