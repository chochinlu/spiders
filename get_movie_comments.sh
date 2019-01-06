#!/bin/bash

fileTypeName="json"

echo ">> Choose your export type: [1]json [2]csv  (Deafault: json)"
read -r fileType
if [ "$fileType" = "2" ]; then
  fileTypeName="csv"
fi

echo "You choose $fileTypeName type"

echo ">> Enter your filename: "
read -r fileName

build=$fileName.$fileTypeName
echo "Export result to $build...."

rm -r "$build"
scrapy crawl movie -o "$build" -s FEED_EXPORT_ENCODING=utf-8 
echo "Done"