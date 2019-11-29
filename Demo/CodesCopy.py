# _*_ coding:utf-8 _*_

import os
import getopt
import sys


class CodesCopyer:

    def __init__(self, root_path):
        self.root_path = root_path
        self.code_formats = [".h", ".m", ".mm", ".c", ".cpp"]

    def list_root_dir(self):
        dirs = os.listdir(self.root_path)
        dirs.sort()

        code_dir_list = []
        for item in dirs:
            path = os.path.join(self.root_path, item)
            if os.path.isdir(path):
                print('code_dir_item' + path)
                code_dir_list.append(path)

        return code_dir_list

    def get_all_code_files(self, code_path):
        code_files = []
        code_lists = os.listdir(code_path)
        code_lists.sort()

        for lists in code_lists:
            path = os.path.join(code_path, lists)
            if os.path.isfile(path):
                if os.path.splitext(path)[1] in self.code_formats:
                    code_files.append(path)

            if os.path.isdir(path):
                for child_code_path in self.get_all_code_files(path):
                    code_files.append(child_code_path)

        return code_files

    def copy_codes_to_text_file(self, code_files, code_root_path):
        f = open(self.root_path + ".txt", 'a')

        f.write('************** ' + code_root_path + ' start ***************** \n\n')

        for file in code_files:
            code_f = open(file, 'r')
            f.write(code_f.read())

        f.write('************** ' + code_root_path + ' end ***************** \n\n')
        f.close()

    def execute_copy(self):
        out_put_path = self.root_path + ".txt"
        if os.path.exists(out_put_path):
            os.remove(out_put_path)

        code_path_list = self.list_root_dir()
        for code_path in code_path_list:
            print(code_path)
            code_file_list = self.get_all_code_files(code_path)
            self.copy_codes_to_text_file(code_file_list, code_path)



def usage():
    print("usage: -copy 'code_path'")


def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'c', ['copy'])
    except getopt.GetoptError:
        usage()
        sys.exit()
    for opt, arg in opts:
        if opt in ['-c', '--copy']:
            code_path = args[0]
            code_copyer = CodesCopyer(code_path)
            code_copyer.execute_copy()
            sys.exit()
        else:
            print("Error: invalid parameters")
            usage()
            sys.exit()

if __name__ == '__main__':
    main(sys.argv)
