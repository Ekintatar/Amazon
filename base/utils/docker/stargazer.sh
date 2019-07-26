#!/usr/bin/env bash

usage() {

    echo "Usage: bash stargazer.sh [OPTIONS]"
    echo
    echo "Options:"
    echo "  --node | -n       node count for creating selenium grid, default is 1"
    echo "  --case | -c       which case(s) you want to run, default run all cases"
    echo "  --static| -s      task id for host file"
    echo "  --type| -t      type of running automation"
}

OPTIONS=$(getopt -o n:c:a:s:t:h -l node:,case:,automation:,static:,type:,help: -- "$@")

if [[ $? -ne 0 ]]; then
  usage
  exit 1
fi

eval set -- ${OPTIONS}
type="test"
node_count="1"
static="local"
while true; do
  case "$1" in
    -n|--node) node_count="$2" ; shift ;;
    -c|--case)  case="$2" ; shift;;
    -s|--static) static="$2" ; shift ;;
    -t|--type) type="$2" ; shift ;;
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

#python -m get_ready_to_test.txt  => This line will be developed

curl -X GET "http://inshoppingcart.api.sociaplus.com/gen-partner-js.php"
curl -X GET "http://shopbagg.api.sociaplus.com/gen-partner-js.php"

if [[ type -eq "test" ]] | [[ type -eq "local" ]]; then
bash ocean.sh --static ${static} --env ${type}
fi

cd .. && cd .. && cd ..

find . -name \*.pyc -delete
find base/utils/error_records/ -name "*.html" -delete
find base/utils/error_records/screenshots/ -name "*-*.png" -delete

touch base/utils/error_records/grid_result.txt && rm base/utils/error_records/grid_result.txt
touch base/utils/error_records/grid_result.txt

node_count=${node_count} case="${case}" nohup docker-compose up --build --abort-on-container-exit --scale chrome_node=${node_count} > base/utils/error_records/nohup.out 2> base/utils/error_records/nohup.err < /dev/null &

echo "Stargazer has just triggered ATLAS project in ${node_count} node(s)"
