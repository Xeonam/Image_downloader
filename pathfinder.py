from pathlib import Path
from googletrans import Translator
import platform
import subprocess




def get_folder_path():
    operating_system = platform.system()
    if operating_system == "Linux":
        try:
            folder = subprocess.run(["xdg-user-dir", "DOWNLOAD"],
                                    capture_output=True, text=True).stdout.strip("\n")
        except FileNotFoundError:  # if the command is missing
            import os.path
            folder = os.path.expanduser("~/Downloads")

        return folder
    else:
        translator = Translator()
        downloads = "Downloads"
        downloads_path = str(Path.home() / downloads)
        if str(downloads_path.split("\\")[-1]) != downloads:
            en_path = translator.translate(str(downloads_path.split("\\")[-1]), dest="en")
            if en_path.text == "downloads" or en_path.text == "Downloads":
                downloads_path = str(Path.home() / str(en_path.text))
        return downloads_path

print(get_folder_path())