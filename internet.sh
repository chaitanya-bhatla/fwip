#!/bin/bash
echo 'Creating Mangle Entry for Https Restriction......'
sleep 5
echo 'avadesh1997'| sudo -S iptables -A POSTROUTING -t nat -o enp2s0 -j MASQUERADE
echo 'avadesh1997'| sudo -S iptables -t mangle -N internet
echo 'avadesh1997'| sudo -S iptables -t mangle -A PREROUTING -i wlpKB5s0 -p tcp -m tcp --dport 443 -j internet
echo 'avadesh1997'| sudo -S iptables -t mangle -A internet -j MARK --set-mark 99
echo 'avadesh1997'| sudo -S iptables -t nat -A PREROUTING -i wlp5s0 -p tcp -m mark --mark 99 -m tcp --dport 443 -j DNAT --to-destination 0.0.0.0:8000
echo 'avadesh1997'| sudo -S iptables -t nat -A PREROUTING -i wlp5s0 -p tcp -m mark --mark 99 -m tcp --dport 80 -j DNAT --to-destination 0.0.0.0:8000


echo 'Done for now....'
