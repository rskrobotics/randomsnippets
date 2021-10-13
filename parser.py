from datetime import datetime


class File:
    def __init__(self, line):
        self.owner = line[0:5]
        self.executable = line[9] == "x"
        self.date = datetime.strptime(str(line[11:22]), "%d %b %Y")
        self.size = int(line[23:32])


class FileFolder:
    def __init__(self):
        self.file_list = []
        self.magicnumber = 14*2**20;
    def add_if_eligible(self, file):
        if file.owner == "admin" and file.executable \
                and file.size < self.magicnumber:
            self.file_list.append(file)

    def find_last_modified(self):
        return min(self.file_list, key=lambda x: x.date).date


def solution(x):
    lines = x.split("\n")
    file_folder = FileFolder()

    for line in lines:
        file_folder.add_if_eligible(File(line))
    return file_folder.find_last_modified().strftime("%Y %b %d")


if __name__ == '__main__':
    inp_str = ""
    owner = ["admin"] * 5 + ["jane"] * 2 + ["admin"]
    perms = ["-wx", "r-x", "--x", "-w-", "--x", "--x", "-w-", "rwx"]
    date = ["29 Sep 1983", "23 Jun 2003", "02 Jul 1997", "15 Feb 1971",
            "15 May 1979", "04 Dec 2010", "08 Feb 1982", "25 Dec 1952"]
    size = ["833", "854016", "821", "23552", "645922816", "93174", "681574400",
            "14680064"]
    name = ["source.h", "blockbuster.mpeg", "delete-this.py", "library.dll",
            "logs.zip", "old-photos.rar", "important.java", "to-do-list.txt"]

    for i in range(len(owner)):
        inp_str = inp_str + f"{owner[i]:<6}" + " " + f"{perms[i]}" \
                  + " " + f"{date[i]}" + f"{size[i]:>10}" + " " \
                  + f"{name[i]}\n"
    inp_str = inp_str.strip("\n")
    print(inp_str)
    print(solution(inp_str))

