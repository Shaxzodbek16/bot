#!/bin/bash

echo 'localserver is starting...'
sleep 1

echo "localserver is running..."

sleep 2

telegram-bot-api/bin/telegram-bot-api --local --api-id=26058376 --api-hash=89ddc1e628e7929ec2a784b2e6826ba1

echo "localserver is stopping..."

sleep 2

echo "localserver stopped successfully"