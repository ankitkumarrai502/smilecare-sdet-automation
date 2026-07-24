"""
Central place for environment configuration.
We'll actually wire this up to python-dotenv in Week 4 — for now it's just
here so you can see where config lives in a real framework.
"""

import os

BASE_URL = os.getenv("BASE_URL", "https://www.smilecaremedicine.com")
API_BASE_URL = os.getenv(
    "API_BASE_URL", "https://www.smilecaremedicine.com/hcgi/platform/api"
)
