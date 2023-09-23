#!/bin/sh

sudo -s

echo "r/R, g/G, y/Y, b/B, o/O, or w/W for ON/OFF for that light..."

while true
do
    read -s -n 1 key
    case $key in
        r)
            python3 LED_TEST1.pyw r on
            ;;
        R)
            python3 LED_TEST.pyw r off
            ;;
        g)
            python3 LED_TEST1.pyw g on
            ;;
        G)
            python3 LED_TEST1.pyw g off
            ;;
        y)
            python3 LED_TEST1.pyw y on
            ;;
        Y)
            python3 LED_TEST1.pyw y off
            ;;
        b)
            python3 LED_TEST1.pyw y on
            ;;
        B)
            python3 LED_TEST1.pyw b off
            ;;
        o)
            python3 LED_TEST1.pyw o on
            ;;
        O)
            python3 LED_TEST1.pyw o off
            ;;
        w)
            python3 LED_TEST1.pyw w on
            ;;
        W)
            python3 LED_TEST1.pyw w off
            ;;
    esac