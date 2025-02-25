import pytest
import os
import tempfile
from datetime import datetime
import time
from unittest.mock import patch
from main import get_name_gnupghome, generate_key_pair, get_name_gnupghome
from freezegun import freeze_time


@freeze_time(time_to_freeze="2025-02-25T12:00:00")
def test_get_name_gnupghome():
    entity = "entity"
    name = "name"
    name_key = get_name_gnupghome(entity, name)
    assert name_key == f"{entity}_2025_02_25_{time.strftime('%H_%M_%S')}_{name}"