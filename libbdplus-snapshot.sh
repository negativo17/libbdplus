#!/bin/sh
git clone -v https://git.videolan.org/git/libbdplus.git

cd libbdplus

COMMIT=$(git rev-list HEAD -n1)
SHORTCOMMIT=$(echo ${COMMIT:0:7})
DATE=$(git log -1 --format=%cd --date=short | tr -d \-)
#rm -fr .git
cd ..

printf "Creating tarball... "
tar -cJf libbdplus-$SHORTCOMMIT.tar.xz libbdplus
rm -fr libbdplus
printf "done.\n"

echo %global commit0 $COMMIT
echo %global date $DATE
