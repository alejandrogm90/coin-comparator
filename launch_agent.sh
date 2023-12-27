#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "$DIR_HOME/src/commons/common_functions.sh"
DIR_LOG="`dirname $DIR_HOME`/log"
SCRIPT_NAME="`getJustStriptName $0`"
export LOG_FILE="${DIR_LOG}/${SCRIPT_NAME}_`date +%F`.log"
declare -A script_info
export script_info=(
	[name]="${SCRIPT_NAME}"
	[location]="${DIR_HOME}"
	[description]="A simple monthly script to get al data of one month"
	[calling]="./`getScriptName $0`"
)

# Show main script info
showScriptInfo

# Main
if [ $# -ne 4 ] ; then
    showError 1 "Number of incorrect parameters. [AGENT] [COIN_NAME] [INITIAL_COINS] [INITIAL_CASH]"
else
    COINS=$3
    CASH=$4
    for c_date in `getAllDatesOfOneMonth 2022 3` ; do
        reaction=`$1 $c_date $2 $CASH $COINS`
        CASH=`echo "$reaction" | cut -d'|' -f3`
        COINS=`echo "$reaction" | cut -d'|' -f4`
        showInfo "$reaction"
    done
fi