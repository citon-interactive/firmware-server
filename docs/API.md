#  Cloud web-app API

This document provides an overview of the API endpoints available in the Citon firmware server. The API allows clients to interact with the server to manage devices, firmware updates, and other related functionalities.

## POST /login
Authenticate a user and obtain a session token.

## GET /firmware/queue
Retrieve the list of firmware updates queued for devices in order of which they were uploaded and with timestamps of when they were uploaded.

## GET /firmware/{mac_addr}
Returns the binary firmware file for the device with the specified MAC address if an update is available.