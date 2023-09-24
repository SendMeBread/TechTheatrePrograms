#! /usr/bin/bash

echo "r/R, g/G, y/Y, b/B, o/O, or w/W for ON/OFF for that light..."

while true
do
    read -s -n 1 key
    case $key in
        r)
            sudo python3 LED_TEST1.pyw r on
            ;;
        R)
            sudo python3 LED_TEST.pyw r off
            ;;
        g)
            sudo python3 LED_TEST1.pyw g on
            ;;
        G)
            sudo python3 LED_TEST1.pyw g off
            ;;
        y)
            sudo python3 LED_TEST1.pyw y on
            ;;
        Y)
            sudo python3 LED_TEST1.pyw y off
            ;;
        b)
            sudo python3 LED_TEST1.pyw y on
            ;;
        B)
            sudo python3 LED_TEST1.pyw b off
            ;;
        o)
            sudo python3 LED_TEST1.pyw o on
            ;;
        O)
            sudo python3 LED_TEST1.pyw o off
            ;;
        w)
            sudo python3 LED_TEST1.pyw w on
            ;;
        W)
            sudo python3 LED_TEST1.pyw w off
            ;;
    esac
done