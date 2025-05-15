# move files in a directory based on their extensions and suppress errors
# Usage: ./move_files.sh
mv *.py python/ 2>/dev/null
mv *.cpp cpp/ 2>/dev/null
mv *.java java/ 2>/dev/null
