#!/bin/bash
# 
# Command-Line for service
# check_flexlm_stat.sh!<FlexLicToCheck>!<min>!<warn>|<crit>
#
# B. Nielsen
#

usage()
{
cat << EOF

usage: `basename $0` -f [license] -m [minlevel] -w [warninglevel] -c [criticallevel]

Check usage of any flexlm license; against a Min, Warn and Critical threshold.

OPTIONS:
   -h      Show this message
   -f      File to check in flexlm. i.e. MATLAB vs say a toolbox.
   -m      Minimum warning level. Warn when below this number. Could be 0.
   -w      Warning level. Warn as critical level is approached.
   -c      Critical level. Critical usage mass has been reached.
EOF
}

EXPECTED_ARGS=8
if [ $# -ne $EXPECTED_ARGS ]
then
  usage
  exit 3
fi

while getopts "hf:m:w:c:" OPTION
do
     case $OPTION in
         h)
             usage
             exit 3
             ;;
         f)
             LIC=$OPTARG
             ;;
         m)
             MIN=$OPTARG
             ;;
         w)
             WARN=$OPTARG
             ;;
         c)
             CRIT=$OPTARG
             ;;
         ?)
             usage
             exit 3
             ;;
     esac
done

if [ "$MIN" -gt "$WARN" ]; then
        echo "Unknown: [minlevel] must be smaller than [warninglevel]"
        exit 3
fi

if [ "$WARN" -gt "$CRIT" ]; then
        echo "Unknown: [warninglevel] must be smaller than [criticallevel]"
        exit 3
fi

USED=`lmstat -f $LIC  | grep "Users of MATLAB" | awk '{print $11}'`

# Greater than or equal to warn level.
if [[ "$USED" -eq "$WARN" || "$USED" -gt "$WARN" ]]; then
		# and less than critical level, then warn.
        if [ "$USED" -lt "$CRIT" ]; then
                echo "FLEXlm Warning: License usage is in warning range (min=$MIN, used=$USED, warn=$WARN, crit=$CRIT)"
                exit 1
		# if not less than critical (already greater than warn), then notify critical.
        else
		        echo "FLEXlm Critical: License usage has reached a critical level (min=$MIN, used=$USED, warn=$WARN, crit=$CRIT)"
                exit 2
        fi
 # Less than warning level, check for a bottom minimum to be above.
 elif [[ "$USED" -lt "$MIN" || "$USED" -eq "$MIN" ]]; then
        echo "FLEXlm Warning: Number of licenses consumed seems to small, check flexlm  (min=$MIN, used=$USED, warn=$WARN, crit=$CRIT)"
        exit 1
 # Less than warning, and greater than min, then OK.
 elif [[ "$USED" -gt "$MIN" && "$USED" -lt "$WARN" ]]; then
		echo "FLEXlm OK: License usage is Ok. (min=$MIN, used=$USED, warn=$WARN, crit=$CRIT)"
		exit 0
 else
        echo "Unknown error"
        exit 3
fi

