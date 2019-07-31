#!/usr/bin/env bash

usage() {

    echo "Usage: bash ocean.sh [OPTIONS]"
    echo
    echo "Options:"
    echo "  --env| -e      environment type of hosts file"
    echo "  --static| -s      task id for host file"
}

OPTIONS=$(getopt -o e:s:h -l env:,static:,help: -- "$@")

if [[ $? -ne 0 ]]; then
  usage
  exit 1
fi


eval set -- ${OPTIONS}
env="local"
static="local"
while true; do
  case "$1" in
    -e|--env) env="$2" ; shift ;;
    -s|--static) static="$2" ; shift ;;
    -h|--help)   usage ;exit ;;
    --)        shift ; break ;;
    *)         echo "unknown option: $1" ; exit 1 ;;
  esac
  shift
done

if [[ $# -ne 0 ]]; then
  echo "unknown option(s): $@"
  usage
  exit 1
fi

nginx_ip="127.0.0.1"

if [[ env -eq "test" ]]; then
nginx_ip="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx-integrated)"
fi

echo "127.0.0.1 localhost
${nginx_ip} shopbagg.inone.useinsider.com inshoppingcart.inone.useinsider.com
${nginx_ip} api.sociaplus.com shopbagg.api.sociaplus.com inshoppingcart.api.sociaplus.com
${nginx_ip} api.useinsider.com shopbagg.api.useinsider.com inshoppingcart.api.useinsider.com
${nginx_ip} static.api.sociaplus.com ${static}.static.api.sociaplus.com
${nginx_ip} static.api.useinsider.com ${static}.static.api.useinsider.com
${nginx_ip} panel.sociaplus.com sppanel.sociaplus.com gachapon.useinsider.com
${nginx_ip} alfred.api.sociaplus.com alfred.api.useinsider.com
" > hosts.txt
