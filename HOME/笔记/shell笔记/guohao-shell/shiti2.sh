 #!/bin/bash

#  讲文件夹中的所有后缀为.sh的文件改名为.shell，包含其子文件夹

#cd /home/jason/桌面
#mkdir  dir1
#cd /home/jason/桌面/dir2

set -x
num=`ls -R dir1`
echo $num

for $i in $num
do
    echo $i
    #cp *.sh  .shell
done
