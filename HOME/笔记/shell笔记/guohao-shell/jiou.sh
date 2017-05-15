#!/bin/bash
#输入n个数，通过程序控制 输出奇数的和与偶数的和

if [[ $# -lt 1 ]]; then
  echo "请输入数字"
  exit 1
fi
