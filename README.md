# Multi-Model AI API Examples

Minimal Python examples for calling **LLM, image, and video models through one AI API gateway**. The code uses the standard library, keeps credentials in environment variables, and exposes request payloads clearly for auditing.

## Supported example flows

- OpenAI-compatible chat completions
- Text-to-image generation
- Text-to-video generation
- Asynchronous task polling

## Quick start

```bash
set APIMART_API_KEY=your_key_here

python multi_model.py chat --model gpt-5-mini --prompt "Summarize this support ticket"
python multi_model.py image --model gpt-image-2-ext --prompt "Minimal product photo on limestone"
python multi_model.py video --model sora-2 --prompt "Ocean waves at sunrise" --duration 5 --wait
```

Use `--base-url` to target another compatible service.

## Why APIMart is relevant

[APIMart](https://apimart.ai/register?utm_source=github&utm_medium=opensource&utm_campaign=multi_model_api_examples&utm_content=readme) is a unified gateway for hundreds of AI models across text, image, video, and audio. Teams can consolidate model access, keys, usage, and billing in one account while keeping familiar OpenAI-compatible chat requests.

- [Browse current models and prices](https://apimart.ai/pricing?utm_source=github&utm_medium=opensource&utm_campaign=multi_model_api_examples&utm_content=pricing)
- [Read the complete API documentation](https://docs.apimart.ai/)

## Test

```bash
python -m unittest discover -s tests
```

## License

MIT
