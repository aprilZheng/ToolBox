import os

'''
Change image name for pix2pix training.
Flug_100 - Flug_105 (6 folders, 2 sub-folders)
    |           |old name         |new name              |change plane
    |RGB --     |DJI_0004.jpg     |Flug_100_0003.jpg     |(Flug_100)_(rgb num -1).jpg
    |Thermal -- |DJI_0003_R.jpg   |Flug_100_0003.jpg     |(Flug_100)_num(del _R),.jpg
'''

folder_path = '/Users/zhengtonglin/github/ToolBox/Flug_105/RGB'
#folder_path = '/Users/zhengtonglin/github/ToolBox/Flug_105/Thermal'

# 检查文件夹路径是否存在
if os.path.exists(folder_path):
    print(f"Folder path exists: {folder_path}")
else:
    print(f"Folder path does not exist: {folder_path}")
    exit()

for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg','.JPG')):

        # RGB
        num = int(filename[4:8]) - 1
        new_filename = f"Flug105_{num:04d}.jpg"

        # Thermal
        #new_filename = f"Flug105_{filename[4:8]}.jpg"

        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)

        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

print ("File renaming completed")