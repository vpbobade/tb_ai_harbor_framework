import requests
import subprocess
import time

def test_service_runs():

    proc = subprocess.Popen(["bash","/app/start.sh"])

    time.sleep(5)

    r = requests.get("http://localhost:8000/health")

    assert r.status_code == 200
    assert r.json()["status"] == "ok"

    proc.kill()
