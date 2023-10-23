import subprocess

def open_visual_studio_code():
    try:
        subprocess.run(["code"])
    except FileNotFoundError:
        print("Visual Studio Code is not installed or not in your system's PATH.")

if __name__ == "__main__":
    open_visual_studio_code()