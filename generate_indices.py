# -*- coding: UTF-8 -*-

import os
import datetime
import shutil
import sys
import fnmatch


main_index_example_head_file_path = "./source/index.rst.example.head"
main_index_example_tail_file_path = "./source/index.rst.example.tail"
main_index_file_path = "./source/index.rst"
rst_source_path = "./source"


def commonLog(str):
	sys.stderr.flush()
	sys.stdout.flush()
	print('[generate_indices]: ' + str)
	sys.stdout.flush()


def generate_indices_dir(dir_name):
	full_path = os.path.join(rst_source_path, dir_name)
	output = ""
	for root, dirnames, filenames in os.walk(full_path):
		for filename in fnmatch.filter(filenames, '*.rst'):
			path = "./" + os.path.relpath(os.path.join(root, filename), './source/').replace("\\","/")
			if(path.endswith(".rst")):
				path = path[:-4]
			commonLog("handle file: " + path)
			output = output + ":doc:`" + path + "`\n\n"

	return output


def generate_indices():
	if(not os.path.exists(rst_source_path)):
		commonLog("Error: rst_source_path:" + rst_source_path + " not exists!!!")
		return

	if(not os.path.exists(main_index_file_path)):
		commonLog("Error: main_index_file_path:" + main_index_file_path + " not exists!!!")
		return

	if(not os.path.exists(main_index_example_head_file_path)):
		commonLog("Error: main_index_example_head_file_path:" + main_index_example_head_file_path + " not exists!!!")
		return

	if(not os.path.exists(main_index_example_tail_file_path)):
		commonLog("Error: main_index_example_tail_file_path:" + main_index_example_tail_file_path + " not exists!!!")
		return

	contents = os.listdir(rst_source_path)

	output = ""
	for item in contents:
		if os.path.isdir(os.path.join(rst_source_path, item)):
			output += generate_indices_dir(item)

	templateHeadFile = open(main_index_example_head_file_path, mode="r", encoding="utf-8")
	templateTailFile = open(main_index_example_tail_file_path, mode="r", encoding="utf-8")

	outputFile = open(main_index_file_path, mode="w", encoding="utf-8")

	outputFile.write(templateHeadFile.read())
	outputFile.write("\n")
	outputFile.write(output)
	outputFile.write("\n")
	outputFile.write(templateTailFile.read())


if __name__=="__main__":
	generate_indices()