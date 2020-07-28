#!/bin/sh
clear
echo "Start Emulator"
read -r -p "Enter Max number of Tasks per Cluster:" t
read -r -p "Max Time between Tasks (in secs):" tt
read -r -p "Enter Max number Clusters:" c
read -r -p "Max Time between Clusters (in secs):" ct

python3 emulator.py --numberoftasks "$t" --numberofclusters "$c"  --tasktime "$tt" --clustertime "$ct"

