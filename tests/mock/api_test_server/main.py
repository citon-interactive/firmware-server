from fastapi import FastAPI, Header, HTTPException
from src.api.models import * 
import secrets

app = FastAPI()

TEST_USERNAME = "testuser"
TEST_PASSWORD = "testpass"
TOKEN = secrets.token_hex(16)
TEST_MAC_ADDR_1 = "AA:BB:CC:DD:EE:FF"
TEST_MAC_ADDR_2 = "11:22:33:44:55:66"
TEST_FIRMWARE_1 = b'\x00\x01\x02\x03\x04'
TEST_FIRMWARE_2 = b'\x05\x06\x07\x08\x09'

@app.post("/login")
async def login(body: LoginPostRequestBody) -> LoginPostResponseBody:
    global TOKEN
    if body.username == TEST_USERNAME and body.password == TEST_PASSWORD:
        TOKEN = secrets.token_hex(16)
        return LoginPostResponseBody(success=True, session_token=TOKEN)
    else:
        return LoginPostResponseBody(success=False, session_token="")

@app.get("/firmware/queue")
async def get_firmware_queue(authorization: str = Header(None)) -> FirmwareQueueGetResponseBody:
    if authorization != "Bearer " + TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return FirmwareQueueGetResponseBody(queue=[TEST_MAC_ADDR_1, TEST_MAC_ADDR_2])

@app.get("/firmware")
async def get_firmware(macc_addr: str, authorization: str = Header(None)) -> FirmwareGetResponseBody:
    if authorization != "Bearer " + TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if macc_addr == TEST_MAC_ADDR_1:
        return FirmwareGetResponseBody(firmware=TEST_FIRMWARE_1)
    elif macc_addr == TEST_MAC_ADDR_2:
        return FirmwareGetResponseBody(firmware=TEST_FIRMWARE_2)
    else:
        raise HTTPException(status_code=404, detail="Firmware not found, for this MAC address: " + macc_addr)