import loraclip
import sys


def test_lora_modes(mode):
	model, preprocess = loraclip.load("ViT-B/16", device="cpu", r=4, lora_mode=mode)
	loraclip.print_trainable_parameters(model)


if __name__ == "__main__":
    mode = sys.argv[1]
    test_lora_modes(mode)
