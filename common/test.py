from common.basePage import BasePage
import os





def count_lines(file_path):
    with open(file_path, 'r', encoding='gbk', errors='ignore') as file:
        count = sum(1 for line in file if line.strip() != '')
    return count


def count_code_lines(directory):
    total_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                count = count_lines(file_path)
                total_count += count
    return total_count



if __name__ == '__main__':
    project_directory = 'D:\FishonTestProject'
    code_line_count = count_code_lines(project_directory)
    print(f"Total code lines: {code_line_count}")




















