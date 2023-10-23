import subprocess
import webbrowser

def open_visual_studio_code():
    try:
        subprocess.run(["code"])
    except FileNotFoundError:
        print("Visual Studio Code is not installed or not in your system's PATH.")

def open_browser():
    try:
        browser = webbrowser.get('safari')
        browser.open('http://google.com')
        browser.open_new_tab('http://youtube.com')
    except webbrowser.Error:
        print("Browser control error")

if __name__ == "__main__":
    open_visual_studio_code()
    open_browser()