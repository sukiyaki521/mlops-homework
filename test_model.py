import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from evaluate import evaluate_accuracy

def test_accuracy():
    acc = evaluate_accuracy()
    assert acc >= 0.85, f"精度不足: {acc}"
