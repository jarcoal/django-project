#!/bin/bash
REMAP_SIGTERM=SIGQUIT NEW_RELIC_CONFIG_FILE=newrelic.ini \
    newrelic-admin run-program celery \
    --app=app.celery.app \
    worker \
    --task-events \
    --loglevel=INFO