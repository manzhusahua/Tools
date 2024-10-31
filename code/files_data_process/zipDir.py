<<<<<<< HEAD
import zipfile
import os, sys
import shutil


class ZIPDIR:
    def __init__(self) -> None:
        super().__init__()

    def zipDir(self, dirpath, outFullName):
=======

import zipfile
import os
class ZIPDIR:
    def zipDir(dirpath, outFullName):
>>>>>>> 1b35db3cd0b79daefed15bffcead9194c8165b0b
        """
        压缩指定文件夹
        :param dirpath: 目标文件夹路径
        :param outFullName: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
<<<<<<< HEAD
            fpath = path.replace(dirpath, "")

=======
            fpath = path.replace(dirpath, '')
    
>>>>>>> 1b35db3cd0b79daefed15bffcead9194c8165b0b
            for filename in filenames:
                print(filename)
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

<<<<<<< HEAD
        # shutil.rmtree(dirpath, ignore_errors=True)


INPUT_STEP = None


def init():

    global INPUT_STEP
    INPUT_STEP = ZIPDIR()

    INPUT_STEP.prs_step_init()


def run(mini_batch):

    return INPUT_STEP.prs_step_run(mini_batch)


if __name__ == "__main__":
    zip_Dir = ZIPDIR()
=======
        # shutil.rmtree(dirpath, ignore_errors=True)
>>>>>>> 1b35db3cd0b79daefed15bffcead9194c8165b0b
