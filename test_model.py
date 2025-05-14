def test_accuracy():
    acc = evaluate_accuracy()
    assert acc >= 0.85, f"精度不足: {acc}"
