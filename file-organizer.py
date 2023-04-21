import os
import shutil
import sys

# Allow the user to enter the path they want organized
print("Welcome to File Organizer!")

while True:
    #helps the user avoid errors when entering file paths
    print("Please enter the path of the directory you want to organize:")
    print("Note: For Windows OS, use double backslashes (\\) in the file path.")
    print("      For macOS and Linux, use forward slashes (/) in the file path.")

    file_path = input("> ")

    # Check if the entered path exists
    if not os.path.exists(file_path):
        print("Error: The entered path does not exist. Please try again.")
    else:
        break

print(f'Currently editing the path: {file_path}')
c = input("Are you sure you want to change location of current files? (q to quit)")

if c == "q":
    print("Operation Cancelled")
    sys.exit(1)

#creates a folder for each file
pdf_folder = os.path.join(file_path, 'PDFs')
video_folder = os.path.join(file_path, 'Videos')
audio_folder = os.path.join(file_path, 'Audios')
image_folder = os.path.join(file_path, 'Images')
docs_folder = os.path.join(file_path, 'Word Documents')
zip_folder = os.path.join(file_path, 'ZIPs')
pptx_folder = os.path.join(file_path, 'Powerpoints')

# Create folders if they do not exist
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

if not os.path.exists(video_folder):
    os.makedirs(video_folder)

if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)

if not os.path.exists(zip_folder):
    os.makedirs(zip_folder)

if not os.path.exists(pptx_folder):
    os.makedirs(pptx_folder)

# stores the types of files in separate lists
pdf_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith('.pdf')]
video_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith(('.mp4', '.m4a'))]
audio_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith('.mp3')]
image_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith(('.jpeg', '.jpg', '.png', '.webp'))]
docx_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith(('.docx', '.doc'))]
zip_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith('.zip')]
ppt_files = [os.path.join(file_path, file_name) for file_name in os.listdir(file_path) if file_name.endswith(('.pptx', '.ppt'))]

# moves the files to their respective folders
for pdf_file in pdf_files:
    shutil.move(pdf_file, os.path.join(pdf_folder, os.path.basename(pdf_file)))
for video_file in video_files:
    shutil.move(video_file, os.path.join(video_folder, os.path.basename(video_file)))
for audio_file in audio_files:
    shutil.move(audio_file, os.path.join(audio_folder, os.path.basename(audio_file)))
for image_file in image_files:
    shutil.move(image_file, os.path.join(image_folder, os.path.basename(image_file)))
for docx_file in docx_files:
    shutil.move(docx_file, os.path.join(docs_folder, os.path.basename(docx_file)))
for zip_file in zip_files:
    shutil.move(zip_file, os.path.join(zip_folder, os.path.basename(zip_file)))
for ppt_file in ppt_files:
    shutil.move(ppt_file, os.path.join(pptx_folder, os.path.basename(ppt_file)))

#stores the number of each type of document
num_pdfs = len(pdf_files)
num_videos = len(video_files)
num_audios = len(audio_files)
num_images = len(image_files)
num_docx = len(docx_files)
num_zip = len(zip_files)
num_pptx = len(ppt_files)

#ouputs the length of each
print("Files Organized!")
print(f'There are {num_pdfs} PDFs, {num_docx} word documents, {num_pptx} PDFs, {num_videos} video files, {num_zip} zip files, {num_audios} audio files and {num_images} image files')



