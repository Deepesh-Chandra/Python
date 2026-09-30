import os;
import shutil;

FOLDER_PATH = os.getcwd();

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.sh', '.bat'],
}

for folder in FILE_TYPES.keys():
    folder_path = os.path.join(FOLDER_PATH, folder);
    if not os.path.exists(folder_path):
        os.makedirs(folder_path);

for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    if os.path.isdir(file_path):
        continue;
    
    file_ext = os.path.splitext(file)[1].lower()
    
    for folder, extensions in FILE_TYPES.items():
        
        if file_ext in extensions:
            shutil.move(file, os.path.join(FOLDER_PATH, folder))
            break;



