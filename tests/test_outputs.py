
import subprocess
import requests
import time


def test_service_health():

    p = subprocess.Popen(
        ["python", "/app/app.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(2)

    r = requests.get("http://localhost:8080/health")

    assert r.status_code == 200
    assert r.json()["status"] == "ok"

    p.terminate()
