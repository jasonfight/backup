#!/bin/bash

function fun() {
  echo "hello world"
}
fun                                   #调用函数
echo "this is funtion:`fun`"        #用``来实现函数的调用

a1 () {
echo "nihao"


}
echo  "a1"
echo "`a1`"
