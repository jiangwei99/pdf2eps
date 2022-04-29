import os

def find_pdf(path):
    file_list = []  # 新建一个空列表用于存放文件名
    file_dir = path  # 指定即将遍历的文件夹路径
    for files in os.walk(file_dir):  # 遍历指定文件夹及其下的所有子文件夹
        for file in files[2]:  # 遍历每个文件夹里的所有文件，（files[2]:母文件夹和子文件夹下的所有文件信息，files[1]:子文件夹信息，files[0]:母文件夹信息）
            if os.path.splitext(file)[1] == '.PDF' or os.path.splitext(file)[1] == '.pdf':  # 检查文件后缀名,逻辑判断用==
                # file_list.append(file)#筛选后的文件名为字符串，将得到的文件名放进去列表，方便以后调用
                file_list.append(file_dir + '\\' + file)  # 给文件名加入文件夹路径
    print(file_list)
    return file_list
if __name__ == '__main__':
    pdf_files = find_pdf('pdfs')
    for pdf_name in pdf_files:
        command = 'pdf2eps.bat 1 '+pdf_name
        print(command)
        os.system(command)
