#!/bin/bash
gunicorn --workers=2 app:app