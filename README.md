# LoRA-CLIP: Easy Wrapper for LoRA-ifying CLIP

### Features

1. Dynamic LoRA-layer insertion across image or text encoder, or both encoders.

2. Loads pre-trained OpenAI CLIP weights safely into LoRA-ified model.

3. Loads fine-tuning ready models by correctly un-freezing `positional_embedding`, `logit_scale`, and projections.

Note: We currently only support Vision Transformer models in the LoRA-ification of image encoders. ResNet models will be added soon.

### Usage

```python
import loraclip
import argparse


def test_loraclip(args):
	# Easy-to-use with standard CLIP syntax.
	# 1. Dynamic LoRA rank specification
	# 2. Specify which encoder(s) to LoRA-ify
	model, preprocess = loraclip.load(args.clip_model_name, device=args.device, r=args.lora_rank, lora_mode=args.lora_mode)
	# Utility to preview no. of trainable params along with their % with total params.
	loraclip.print_trainable_parameters(model)


def setup_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--clip-model-name", type=str, default="ViT-B/16")
	parser.add_argument("--device", type=str, default="cuda")
	parser.add_argument("--lora-rank", type=int, default=4)
	parser.add_argument("--lora-mode", type=str, default="vision+text", choices=["vision", "text", "vision+text"])

	args = parser.parse_args()
	return args


if __name__ == "__main__":
    args = setup_args()
    test_loraclip(args)
```

### References

1. <a href="https://github.com/openai/CLIP">https://github.com/openai/CLIP</a>

2. <a href="https://github.com/SivanDoveh/TSVLC">https://github.com/SivanDoveh/TSVLC</a>
