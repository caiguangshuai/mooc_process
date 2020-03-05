import os.path
import shutil

path = "F:\\mooc\\智能交互技术_北京联合大学"
path_length = len(path.split("\\"))


# 移动文件
def move_file(source_file, destination):
    shutil.move(source_file, destination)
    print("%s 移动到 --> %s" % (os.path.basename(source_file), destination))


def scan_and_move_file(path):
    parent_dir = os.path.dirname(path)

    for root, dirs, files in os.walk(path):

        for name in dirs:
            scan_and_move_file(os.path.join(root, name))

        for name in files:
            file = os.path.join(root, name)
            if len(file.split("\\")) - path_length == 3:
                move_file(file, parent_dir)


# 删除空文件夹
def remove_empty_dir(path):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            dir = os.path.join(root, name)
            if not os.listdir(dir):
                os.rmdir(dir)
            print("空文件 %s 已删除！" % dir)


if __name__ == '__main__':
    scan_and_move_file(path)
    remove_empty_dir(path)
