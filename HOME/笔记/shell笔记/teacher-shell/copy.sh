#! /bin/bash

filedir=$HOME/file_dir
dirdir=$HOME/dir_dir

if [ -e $filedir ] && [ -d $filedir ]
then
	rm -rf $filedir
fi

if [ -e $dirdir ] && [ -d $dirdir ]
then
	rm -rf $dirdir
fi

mkdir $filedir
mkdir $dirdir

filelist=`ls`

for file in $filelist
do
	if [ -d $file ]
	then
		cp -a $file  $dirdir

	elif [ -f $file ]
	then
		cp $file  $filedir
	fi
done


tar -cjvf file_dir.tar.bz2   $filedir
mv file_dir.tar.bz2  /home/linux/share/

tar -czvf dir_dir.tar.gz  $dirdir
mv dir_dir.tar.gz  /home/linux/share/

cd /home/linux/share/
tar -xvf  file_dir.tar.bz2
tar -xvf  dir_dir.tar.gz
