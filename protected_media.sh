#!bash/google-cloud-sdk/bin
#!/usr/bin/env python

CUR_DATE=`date +%Y/%m/%d`
CUR_HOUR=`date +%H`
epoch_sec=$(date -jf '%H%M%S' $CUR_HOUR '+%s')
minus_hour=$(( epoch_sec - 3600 ))
PREV_HOUR=$(date -r $minus_hour '+%H')
REPORT_DATE=$(date +%Y%m%d)-$PREV_HOUR

curl https://sdk.cloud.google.com | bash gcloud auth activate-service-account <username>@<domain>.iam.gserviceaccount.com --key-file <Path/To/Key>
gsutil cp gs://<PID>.reports.protected.media/$CUR_DATE/<PID>-$REPORT_DATE.csv <location/to/save/report>

python PM_Cedato_Main.py
