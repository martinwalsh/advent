#!/bin/bash
set -e

SOURCE="$1"
if [ -z "$SOURCE" ]; then
  echo "Usage: $0 path/to/dayNN.ext [content pattern]"
  exit 1
fi

DAY=1
PATTERN="${SOURCE//NN/%02d}"

DEST="$(printf -- "$PATTERN" "$DAY")"
while test -e "$path"; do
  (( ++DAY ))
  DEST="$(printf -- "$PATTERN" "$DAY")"
done

cp -iv "$SOURCE" "$DEST"

shift
while [ -n "$1" ]; do
  REPLACE="$(printf -- "${1//NN/%02d}" "$DAY")"
  sed -i '' "s/$1/${REPLACE}/g" "$DEST"
  shift
done

exit 0
