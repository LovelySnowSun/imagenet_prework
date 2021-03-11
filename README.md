# imagenet_prework

此库中包含imagenet-untar脚本文件与imagenet-val脚本文件

#imagenet-untar脚本文件

输入：已解压的imagenet test文件夹目录，其中应包含1000个压缩包文件

功能：对每一个压缩包创建对应文件夹，并将其解压文件解压到对应的文件夹中，并有进度显示

#imagenet-val脚本文件

输入：ILSVRC2012_devkit_t12.tar 中的ILSVRC2012_devkit_t12文件夹目录与已解压的imagenet val文件夹目录

功能：读取ILSVRC2012_devkit_t12\data中文件对每一个val图片进行检索并在val文件夹中创建相对应的文件夹进行保存
