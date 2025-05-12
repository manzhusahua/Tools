import zipfile
import os, sys
import shutil


class ZIPDIR:
    def __init__(self) -> None:
        super().__init__()

    def zipDir(self, dirpath, outFullName):
        """
        压缩指定文件夹
        :param dirpath: 目标文件夹路径
        :param outFullName: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath, "")

            for filename in filenames:
                if ".wav" in filename:
                    print(filename)
                    zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()

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
    zip_Dir.zipDir(r"C:\Users\v-zhazhai\Desktop\scripts",r"C:\Users\v-zhazhai\Desktop\waves.zip")