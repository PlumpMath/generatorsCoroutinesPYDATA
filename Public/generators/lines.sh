find \( -iname '*.py' -or -iname '*.c' -or -iname '*.cpp' \) -print0 | xargs -d'\0' wc -l | tail -n 1
