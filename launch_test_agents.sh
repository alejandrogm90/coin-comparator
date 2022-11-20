#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "commons/commonFunctions.sh"
SCRIPT_NAME=`getJustStriptName $0`
export LOG_FILE=${DIR_HOME}"/"${SCRIPT_NAME}"_"`date +%F`".log"
SCRIPT_1="./coinlayer/get_day.py"

declare -A script_info
export script_info=(
	[name]="${SCRIPT_NAME}" 
	[location]="${DIR_HOME}" 
	[description]="A simple monthly scrit to get al data of one month" 
	[calling]="./`getStriptName $0`"
)

showScriptInfo

#echo "" > $LOG_FILE

CASH=100
COINS=100

for cDate in `getAllDatesOfOneMonth 2022 3` ; do
	#reaction=`reactive_agent/agent_1.py $cDate BTC $CASH $COINS`
	#reaction=`reactive_agent/agent_2.py $cDate BTC $CASH $COINS 0.02`
	#reaction=`reactive_agent/agent_3.py $cDate BTC $CASH $COINS 0.02`
	reaction=`reactive_agent/agent_4.py $cDate BTC $CASH $COINS 0.02`
	echo "$reaction"
	CASH=`echo $reaction | cut -d'|' -f3`
	COINS=`echo $reaction | cut -d'|' -f4`
done