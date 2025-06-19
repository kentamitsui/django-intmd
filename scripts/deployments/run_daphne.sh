#!/bin/bash
export DJANGO_SETTINGS_MODULE=django_intmd.settings.base
export PYTHONPATH=/django_intmd

daphne -b 0.0.0.0 -p 8001 \
    -v 2 \
    --access-log - \
    django_intmd.asgi:application
