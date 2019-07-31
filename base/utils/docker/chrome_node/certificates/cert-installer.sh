rm -rf ~/.pki/ &&
sudo apt update && sudo apt install libnss3-tools &&
mkdir -p ~/.pki/nssdb && chmod 700 ~/.pki/nssdb && certutil -d sql:$HOME/.pki/nssdb -N --empty-password &&
certutil -d sql:$HOME/.pki/nssdb -A -t 'P,,' -n 'USEINSIDER_STAGING' -i /etc/certificates/useinsider.crt &&
certutil -d sql:$HOME/.pki/nssdb -A -t 'P,,' -n 'SOCIAPLUS_STAGING' -i /etc/certificates/sociaplus.crt
