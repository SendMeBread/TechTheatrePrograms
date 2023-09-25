#! /usr/bin/bash

echo "o/O, w/W, e/E, r/R, v/V, x/X, n/N, g/G, i/I, t/T, l/L, 2/@, 5/%, 4/&, f/F, s/S for ON/OFF for that light..."

while true
do
    read -s -n 1 key
    case $key in
        o)
            sudo python3 Max.pyw p1 on
            ;;
        O)
            sudo python3 Max.pyw p1 off
            ;;
        w)
            sudo python3 Max.pyw p2 on
            ;;
        W)
            sudo python3 Max.pyw p2 off
            ;;
        e)
            sudo python3 Max.pyw p3 on
            ;;
        E)
            sudo python3 Max.pyw p3 off
            ;;
        r)
            sudo python3 Max.pyw p4 on
            ;;
        R)
            sudo python3 Max.pyw p4 off
            ;;
        v)
            sudo python3 Max.pyw p5 on
            ;;
        V)
            sudo python3 Max.pyw p5 off
            ;;
        x)
            sudo python3 Max.pyw p6 on
            ;;
        X)
            sudo python3 Max.pyw p6 off
            ;;
        n)
            sudo python3 Max.pyw p7 on
            ;;
        N)
            sudo python3 Max.pyw p7 off
            ;;
        g)
            sudo python3 Max.pyw p8 on
            ;;
        G)
            sudo python3 Max.pyw p8 off
            ;;
        i)
            sudo python3 Max.pyw p9 on
            ;;
        I)
            sudo python3 Max.pyw p9 off
            ;;
        t)
            sudo python3 Max.pyw p10 on
            ;;
        T)
            sudo python3 Max.pyw p10 off
            ;;
        l)
            sudo python3 Max.pyw p11 on
            ;;
        L)
            sudo python3 Max.pyw p11 off
            ;;
        2)
            sudo python3 Max.pyw p12 on
            ;;
        @)
            sudo python3 Max.pyw p12 off
            ;;
        5)
            sudo python3 Max.pyw p13 on
            ;;
        %)
            sudo python3 Max.pyw p13 of
            ;;
        4)
            sudo python3 Max.pyw p14 on
            ;;
        $)
            sudo python3 Max.pyw p14 off
            ;;
        f)
            sudo python3 Max.pyw p15 on
            ;;
        F)
            sudo python3 Max.pyw p15 off
            ;;
        s)
            sudo python3 Max.pyw p16 on
            ;;
        S)
            sudo python3 Max.pyw p16 off
            ;;
    esac
done