#!/bin/sh

RED='\033[31;47m'
NC='\033[0m'

PROGNAME=$(basename $0)

error_exit()
{
	echo ${RED} $(date +"%D %T") "${PROGNAME}: ${1:="Unknown Error"}" ${NC} 1>&2
	tput sgr0
	exit 1
}

echo $(date +"%D %T") "Example of error with line number and message"
error_exit "$LINENO: An error has occured."