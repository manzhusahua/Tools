import os, sys


def get_filelist(chunkpath, outputfile):
    with open(outputfile, "w", encoding="utf8") as s:
        for home, dirs, files in os.walk(chunkpath):
            for filename in files:
                if ".txt" in filename:
                    s.writelines(os.path.join(home, filename) + "\n")


if __name__ == "__main__":
    get_filelist(sys.argv[1], sys.argv[2])
