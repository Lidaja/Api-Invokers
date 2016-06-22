curlId=$(curl --unix-socket /var/run/system-docker.sock -s -H "Content-Type: application/json" -X POST -d  '{"AttachStdin": false, "AttachStdout": true, "AttachStderr": true, "Tty": false, "Cmd": [ "/usr/lib/python2.7/Api-Invokers/invokers/test" ] }' http:/containers/console/exec | jq '.Id' | tr -d '\"')
echo $curlId
command="curl --unix-socket /var/run/system-docker.sock -s -H \"Content-Type: application/json\" -X POST -d '{\"Detach\": false, \"Tty\": true }' http:/exec/$curlId/start"
echo $command
result=$(eval $command)
echo $result
