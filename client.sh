#!/usr/bin/bash
# sh client.sh <wget|curl> <server_ip> <server_port> <downloading_file>

for((i=0;i<10000;i++))
do
        if [ $1 == 'wget' ];then
                wget http://$2:$3/$4 -t 1
        else
                curl -vlf --progress-bar  http://$2:$3/$4 -o abc.dt
        fi
        if [ $? -ne 0 ]; then
                echo "Error!!! Error!!!"
                break
        fi
done

