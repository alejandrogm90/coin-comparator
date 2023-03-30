#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "$DIR_HOME/commons/commonFunctions.sh"
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

# MAIN
if [ $# -ne 4 ] ; then
    showError 1 "Number of incorrect parameters. [AGENT] [COIN_NAME] [INITIAL_COINS] [INITIAL_CASH]"
else
    COINS=$3
    CASH=$4
    for cDate in `getAllDatesOfOneMonth 2022 3` ; do
        #reaction=`reactive_agent/agent_4.py $cDate BTC $CASH $COINS 0.02`
        #reaction=`$1 $cDate $2 $CASH $COINS`
        echo "$1 $cDate $2 $CASH $COINS"
        reaction="$CASH|$COINS|$(( $CASH + 100 ))|$(( $COINS - 10 ))"
        CASH=`echo "$reaction" | cut -d'|' -f3`
        COINS=`echo "$reaction" | cut -d'|' -f4`
        #showInfo "$reaction"
    done
fi