#!/bin/bash

fileTypeName="json"


echo "You choose $fileTypeName type"

echo ">> Enter your filename: "
read -r fileName

build=$fileName.$fileTypeName
echo "Export result to $build...."

rm -r "$build"
scrapy crawl douban_pics -o "$build" 
echo "Done"