from client import TDPSOLA

def main():
    print("=== Testing TD-PSOLA Timescale Modifier ===")
    psola = TDPSOLA()

    test_sig = [1.0, 0.5, -0.5, -1.0] * 8
    stretched = psola.time_stretch(test_sig, pitch_period=4, stretch_factor=2.0)

    print(f"Original length: {len(test_sig)}, Stretched length: {len(stretched)}")
    assert len(stretched) > len(test_sig)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
