#!/bin/bash
set -e

SOURCE="$1"
if [ -z "$SOURCE" ]; then
  echo "Usage: $0 path/to/dayNN.ext [content pattern]"
  exit 1
fi

DAY=1
PATTERN="${SOURCE//NN/%02d}"

# shellcheck disable=SC2059
DEST="$(printf -- "$PATTERN" "$DAY")"
while test -e "$DEST"; do
  (( ++DAY ))
  # shellcheck disable=SC2059
  DEST="$(printf -- "$PATTERN" "$DAY")"
done

cp -riv "$SOURCE" "$DEST"
if [ -d "$SOURCE" ]; then
    DEST="${DEST}/*"
fi

shift
while [ -n "$1" ]; do
  # shellcheck disable=SC2059
  REPLACE="$(printf -- "${1//NN/%02d}" "$DAY")"
  for path in $DEST; do
      sed -i '' "s/$1/${REPLACE}/g" "$path"
  done
  shift
done

exit 0
