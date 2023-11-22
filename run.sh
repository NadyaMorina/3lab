#!/bin/bash
uvicorn --factory app.main:create_app
