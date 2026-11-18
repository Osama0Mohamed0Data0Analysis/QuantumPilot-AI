#!/usr/bin/env python3
"""
QuantumPilot AI - Local API Test Script
Run: python test_local_api.py
Assumes api server running: uvicorn api.index:app --port 8001
"""

import requests
import json
import sys

BASE = "http://localhost:8001"

def test_health():
    r = requests.get(f"{BASE}/api/v1/health")
    print("✅ /health:", r.json())
    return r.status_code == 200

def test_backends():
    r = requests.get(f"{BASE}/api/v1/backends")
    data = r.json()
    print(f"✅ /backends: {len(data)} backends")
    for b in data:
        print(f"   - {b['backend_name']}: T1={b['T1_mean']}us  RO={b.get('readout_error_mean')}")
    return r.status_code == 200

def test_spaceweather():
    r = requests.get(f"{BASE}/api/v1/spaceweather/live")
    data = r.json()
    print(f"✅ /spaceweather/live: kp={data.get('kp_index')}  neutron={data.get('neutron_flux')}")
    return r.status_code == 200

def test_copilot_ar():
    payload = {"intent_text": "أريد أقل تكلفة وتجنب الطقس الشمسي", "kp_index": 2.0, "neutron_flux": 94.6}
    r = requests.post(f"{BASE}/api/v1/copilot/plan", json=payload)
    data = r.json()
    print("✅ /copilot/plan (AR):", data.get("intent", {}).get("type"))
    print("   Plan:", data.get("plan", {}))
    return r.status_code == 200

def test_copilot_en():
    payload = {"intent_text": "cheapest and highest fidelity", "kp_index": 1.5}
    r = requests.post(f"{BASE}/api/v1/copilot/plan", json=payload)
    print("✅ /copilot/plan (EN):", r.json().get("intent", {}).get("type"))
    return r.status_code == 200

def test_mitigation():
    r = requests.get(f"{BASE}/api/v1/mitigation/compare")
    data = r.json()
    s_zne = data.get("results", {}).get("s_zne", {})
    print(f"✅ /mitigation/compare: S-ZNE overhead={s_zne.get('overhead')} ({s_zne.get('advantage', '')})")
    return r.status_code == 200

def test_execute():
    payload = {
        "qasm": "OPENQASM 2.0; include \"qelib1.inc\"; qreg q[2]; creg c[2]; h q[0]; cx q[0],q[1]; measure q[0]->c[0]; measure q[1]->c[1];",
        "backend_name": "ibm_kingston",
        "shots": 1024,
        "mitigation_strategy": "s_zne"
    }
    r = requests.post(f"{BASE}/api/v1/execute/real", json=payload)
    data = r.json()
    print("✅ /execute/real →", data.get("ibm_job_id"), data.get("status"))
    job_id = data.get("ibm_job_id")
    if job_id:
        r2 = requests.get(f"{BASE}/api/v1/jobs/{job_id}")
        print("   Job status:", r2.json().get("status"))
    return r.status_code == 200

def test_generate():
    r = requests.post(f"{BASE}/api/v1/generate", json={"prompt": "Bell state"})
    print("✅ /generate:", r.json().get("code", "")[:60] + "...")
    return r.status_code == 200

if __name__ == "__main__":
    print("=== QuantumPilot AI Local API Test Suite ===\n")
    tests = [test_health, test_backends, test_spaceweather, test_copilot_ar, test_copilot_en, test_mitigation, test_execute, test_generate]
    passed = 0
    for t in tests:
        try:
            if t(): passed += 1
        except Exception as e:
            print(f"❌ {t.__name__} failed: {e}")
    print(f"\n=== {passed}/{len(tests)} tests passed ===")
    if passed == len(tests):
        print("🎉 All core platform endpoints working perfectly!")
    sys.exit(0 if passed == len(tests) else 1)
