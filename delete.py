import os


def delete_file(path, suffix):
    for root, dirs, files in os.walk(path):
        for name in files:
            file = os.path.join(root, name)

            if name.split(".")[-1] == suffix:
                os.remove(file)
                print("删除了 %s " % file)


if __name__ == '__main__':
    path = "E:\\Study\\MOOC"
    suffix = "pdf"

    delete_file(path, suffix)
