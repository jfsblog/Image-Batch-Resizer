import os
from tkinter import filedialog, messagebox
from PIL import Image
import tkinter as tk

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

def select_folder():
    folder_path = filedialog.askdirectory(title="選擇照片所在資料夾")
    if folder_path:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_path)

def batch_resize_images():
    folder_path = folder_path_entry.get()
    if not folder_path:
        messagebox.showerror("錯誤", "請選擇照片所在資料夾")
        return

    new_width = int(new_width_entry.get())

    # 獲取資料夾內所有檔案列表
    file_list = os.listdir(folder_path)

    # 過濾出圖片檔案
    image_files = [file for file in file_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 執行批次轉檔
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        resize_image_width(image_path, new_width)

    messagebox.showinfo("轉檔完成", "圖片批次轉檔完成！")

# 建立Tkinter視窗
root = tk.Tk()
root.title("圖片批次轉檔程式")
root.attributes("-topmost", True)
frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
frame.pack()

h1_font = ("Arial", 20)
h1_label = tk.Label(frame, text="圖片批次轉檔程式", font=h1_font)
h1_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# 資料夾路徑輸入框及瀏覽按鈕
folder_label = tk.Label(frame, text="選擇照片所在資料夾：")
folder_label.grid(row=1, column=0, padx=5, pady=5)

folder_path_entry = tk.Entry(frame)
folder_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

browse_button = tk.Button(frame, text="瀏覽", command=select_folder)
browse_button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W+tk.E)

# 新的寬度輸入框
width_label = tk.Label(frame, text="請輸入照片新的寬度：")
width_label.grid(row=2, column=0, padx=5, pady=5)

new_width_entry = tk.Entry(frame)
new_width_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

# 開始轉檔按鈕
convert_button = tk.Button(frame, text="開始轉檔", command=batch_resize_images, bg='pink')
convert_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky=tk.W+tk.E)

root.mainloop()
