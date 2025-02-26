import pytest
import os
import tempfile
from datetime import datetime
import time
from unittest.mock import patch
from main import get_name_gnupghome, generate_key_pair, get_name_gnupghome
from freezegun import freeze_time


mock_key = {
    "fingerprint": "Fingerprint",
    "keyid": "Key ID",
    "length": "Length",
    "type": "Type",
    "algo": "Algo",
    "date": "Date",
    "expires": "Expires",
    "ownertrust": "Owner Trust",
    "uid": "UID",
    "sig": "Sig",
    "cap": "Cap",
    "issuing_key_fingerprint": "Issuing Key Fingerprint",
    "serial": "Serial",
    "curve": "Curve",
    "compliance": "Compliance",
    "created": "Created",
    "expires": "Expires",
    "flags": "Flags",
    "hash": "Hash",
    "keygrip": "Keygrip",
    "subkey": "Subkey",
    "subkey_fingerprint": "Subkey Fingerprint",
    "subkey_keygrip": "Subkey Keygrip",
    "subkey_type": "Subkey Type",
    "subkey_curve": "Subkey Curve",
    "subkey_created": "Subkey Created",
    "subkey_expires": "Subkey Expires",
    "subkey_flags": "Subkey Flags",
    "subkey_hash": "Subkey Hash",
    "subkey_keygrip": "Subkey Keygrip",
    "subkey_length": "Subkey Length",
    "subkey_sig": "Subkey Sig",
    "subkey_type": "Subkey Type",
    "subkey_usage": "Subkey Usage",
    "subkey_validity": "Subkey Validity",
    "subkey_ownertrust": "Subkey Owner Trust",
    "subkey_revoked": "Subkey Revoked",
    "subkey_revocation_reason": "Subkey Revocation Reason"
}

@freeze_time(time_to_freeze="2025-02-23T22:05")
def test_get_name_gnupghome():
    entity = "entity"
    name = "name"
    name_key = get_name_gnupghome(entity)
    assert name_key == f"{entity} 2025-{time.strftime("%m-%d")}"

@patch("gnupg.GPG")
def test_generate_key_pair(mock_gpg):
    entity = "entity"
    real_name = get_name_gnupghome(entity)
    mock_gpg.return_value.gen_key.return_value = mock_key
    key = generate_key_pair("RSA", 2048, "RSA", "email", entity)
    assert key == mock_key
    