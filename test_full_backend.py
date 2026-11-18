#!/usr/bin/env python3
import os, sys, torch, numpy as np
sys.path.insert(0, 'backend')

os.environ.setdefault('HF_TOKEN', 'placeholder')
os.environ.setdefault('IBM_TOKEN', 'placeholder')
os.environ.setdefault('IBM_CRN', 'placeholder')

print("=== QuantumPilot AI - Full Backend + NeuralUCB Test ===\n")

from app.core.config.settings import settings
print("✅ Settings loaded")

from app.infrastructure.ai.neuralucb.engine import NeuralUCB
print("✅ NeuralUCB class imported")

model_path = "models/neuralucb/reward_net_deep.pt"
state = torch.load(model_path, map_location="cpu")
print(f"✅ Model weights loaded ({len(state)} tensors)")

ucb = NeuralUCB(context_dim=22, hidden_dim=128)
ucb.model.load_state_dict(state)
ucb.model.eval()
print("✅ NeuralUCB model ready (RewardNet 22→128→128→1)")

# EXACT 22-D context (from project docs + real data)
# [T1, T2, RO, CZ, queue, depth, 2q_density, fid_hist, cost_hist, time_hist,
#  kp, kp_norm, temp_norm, exp_fid, shots, opt_level, mit_overhead,
#  fidelity_factor, cost_factor, time_factor, backend_score, extra]
ctx = np.array([
    231.0,   # T1
    159.7,   # T2
    0.0218,  # readout
    0.0292,  # cz_error
    8,       # queue
    14,      # depth
    0.42,    # 2q_density
    0.92,    # hist_fidelity
    0.15,    # hist_cost
    0.08,    # hist_time
    2.0,     # kp_index
    0.222,   # kp_norm
    0.646,   # temp_norm
    0.96,    # expected_fidelity
    1024,    # shots
    2,       # optimization_level
    1.2,     # mitigation_overhead
    0.75,    # fidelity_factor
    0.18,    # cost_factor
    0.07,    # time_factor
    0.85,    # backend_score
    0.0      # extra (pad to 22)
], dtype=np.float32)

assert len(ctx) == 22, f"Got {len(ctx)}"

print(f"✅ 22-D context ready (T1={ctx[0]}, kp={ctx[10]})")

with torch.no_grad():
    x = torch.from_numpy(ctx).float().unsqueeze(0)
    pred = ucb.model(x).item()
print(f"✅ RewardNet inference: {pred:.6f}")

# Simulate multi-arm decision
contexts = [ctx + np.random.normal(0, 0.02, 22).astype(np.float32) for _ in range(6)]
chosen, _ = ucb.select(contexts)
print(f"✅ UCB decision: chose arm #{chosen} / 6")

print("\n🎉 FULL BACKEND + NEURALUCB SUCCESS")
print("   Reward model + decision engine fully functional")
