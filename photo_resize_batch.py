import os
from PIL import Image

def resize_image_width(image_path, new_width):
    # 開啟圖片
    img = Image.open(image_path)

    # 計算新的高度，保持寬高比例不變
    width_percent = (new_width / float(img.size[0]))
    new_height = int((float(img.size[1]) * float(width_percent)))

    # 重新設置圖片大小
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)

    # 儲存新的圖片
    resized_img.save(os.path.splitext(image_path)[0] + "_resized.jpg")

def batch_resize_images(folder_path, new_width):
    # 獲取資料夾內所有檔案列表
    file_list = os.listdir(folder_path)

    # 過濾出圖片檔案
    image_files = [file for file in file_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 執行批次轉檔
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        resize_image_width(image_path, new_width)

# 執行範例
folder_path = input(str("輸入照片所在資料夾："))  # 資料夾路徑
new_width = int(input("請輸入照片新的寬度："))  # 新的寬度
batch_resize_images(folder_path, new_width)
