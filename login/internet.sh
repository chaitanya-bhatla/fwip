#!/bin/bash
echo 'Creating Mangle Entry for Https Restriction......'
sleep 5
echo 'copenhagen1996'| sudo -S iptables -A POSTROUTING -t nat -o enp6s0 -j MASQUERADE
echo 'copenhagen1996'| sudo -S iptables -t mangle -N internet
echo 'copenhagen1996'| sudo -S iptables -t mangle -A PREROUTING -i wlp3s0 -p tcp -m tcp --dport 443 -j internet
echo 'copenhagen1996'| sudo -S iptables -t mangle -A internet -j MARK --set-mark 99
echo 'copenhagen1996'| sudo -S iptables -t nat -A PREROUTING -i wlp3s0 -p tcp -m mark --mark 99 -m tcp --dport 443 -j DNAT --to-destination 10.42.0.1:8000
echo 'copenhagen1996'| sudo -S iptables -t nat -A PREROUTING -i wlp3s0 -p tcp -m mark --mark 99 -m tcp --dport 80 -j DNAT --to-destination 10.42.0.1:8000


echo 'Done for now....'
