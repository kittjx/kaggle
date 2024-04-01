# 读取 train.csv 文件，并按照 ImageFolder 所需的格式重新组织图片和标签

import os  
import pandas as pd  
import shutil  
from pathlib import Path  
  
orig_img_rt_dir = os.path.join('data', 'cifar-10', 'images', 'train')
reorg_img_rt_dir = os.path.join('data', 'cifar-10', 'images', 'train', 'reorg')

csv_path = os.path.join('data', 'cifar-10', 'train.csv')

col_img = 'id'
col_class = 'label'
img_ext = '.png'

# 读取CSV文件
df = pd.read_csv(csv_path)
class_labels = df[col_class].unique()

# 创建所有类别的子目录
os.makedirs(reorg_img_rt_dir, exist_ok=True)  
for label in class_labels:
    os.makedirs(os.path.join(reorg_img_rt_dir, label), exist_ok=True)
  
# 遍历CSV中的每一行  
for index, row in df.iterrows():  
    # 获取图片路径和标签  
    image_id = row[col_img]
    file_name = str(image_id) + img_ext
    image_path = os.path.join(orig_img_rt_dir, file_name)
    label = row[col_class]  
      
    # 构造新路径  
    new_image_dir = os.path.join(reorg_img_rt_dir, label)  
    new_image_path = os.path.join(new_image_dir, file_name)  
      
    # 复制图片到新位置  
    shutil.copy2(image_path, new_image_path)  
  
print(f"Data reorganization completed. New dataset directory: {reorg_img_rt_dir}")