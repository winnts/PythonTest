import string
import random
import commands
import os
import argparse


def string_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_exe(file_name):
    commands.getoutput("pyinstaller --onefile "+file_name)


def run_exe(file_exe):
    for i, each_file in enumerate(file_exe):
        print ('Starting file: ' + each_file)
        commands.getoutput(each_file)


def generate_file(count):
    file_list = []
    for i in range(count):
        file_name = string_generator(8)
        target = open(file_name+".py", 'w')
        target.write("def print_hello():")
        target.write("\n")
        target.write("    print ('"+string_generator(random.randint(0, 300))+"')")
        target.write("\n")
        target.write("\n")
        target.write("print_hello()")
        target.write("\n")
        target.close()
        generate_exe(file_name+".py")
        file_list.append("dist/"+file_name)
        os.remove(file_name+".py")
        os.remove(file_name+".spec")
    return file_list


parser = argparse.ArgumentParser()
parser.add_argument('-files', type=int, default=2)
args = parser.parse_args()
run_exe(generate_file(args.files))
