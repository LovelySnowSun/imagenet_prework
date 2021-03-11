#导入模块
import glob,os,tarfile,time
#文件夹目录
path_home = "D:/imagenet/val"
#获取文件夹中的文件列表
path_list = glob.glob(os.path.join(path_home,'*'))
#遍历
for single_path,i in zip(path_list,range(len(path_list))):
    #以压缩文件名在文件夹下创建子文件夹
    path_dir = os.path.join(path_home,os.path.basename(single_path).split(".")[0])
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    #解压文件夹
    f = tarfile.open(single_path)
    names = f.getnames()
    for name in names:
        f.extract(name, path=path_dir)
    #进度条
    a = "■" * i
    b = "□" * (len(path_list)- i- 1)
    c = ((i+1) / len(path_list)) * len(path_list) * (100/len(path_list))
    print("\r{}{}{:.2f}%".format(a, b, c), end="")
    time.sleep(0.1)
