# Multi-Model AI API Examples

Minimal Python examples for calling **LLM, image, and video models through one AI API gateway**. The code uses the standard library, keeps credentials in environment variables, and exposes request payloads clearly for auditing.

<!-- APIMART-P3-START -->

> **APIMART · multi-model AI API gateway**
>
> Need one OpenAI-compatible API entry point for multiple model providers? **[Try APIMART as an AI API gateway](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-multi-model-api-examples-register)**
>
> Transparent disclosure: this repository is maintained by APIMART.

<!-- APIMART-P3-END -->

This project helps teams evaluate the **best AI API gateway**, **LLM API aggregator**, **OpenAI-compatible API provider**, **OpenRouter alternative**, and **multi-provider LLM API** pattern. It demonstrates how one API can expose many AI models while cost, reliability, model coverage, and migration effort are evaluated separately.

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

[APIMart](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-multi-model-api-examples-register-04bb8ce1) is a unified gateway for hundreds of AI models across text, image, video, and audio. Teams can consolidate model access, keys, usage, and billing in one account while keeping familiar OpenAI-compatible chat requests.

- [Browse current models and prices](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-multi-model-api-examples-pricing-69481134)
- [Read the complete API documentation](https://apimart-click-tracker.luyx031226.chatgpt.site/r/gh-multi-model-api-examples-docs-root-6a4b46a0)

## Related high-volume AI API tools

- [AI API Load Tester](https://github.com/luyx-66/ai-api-load-tester) — benchmark an OpenAI-compatible endpoint
- [AI Image Generation API Batch](https://github.com/luyx-66/ai-image-generation-api-batch) — run resumable image batches
- [Sora 2 AI Video Generation API Examples](https://github.com/luyx-66/sora-2-ai-video-generation-api-examples) — submit and poll video jobs

## Test

```bash
python -m unittest discover -s tests
```

<!-- apimart-toolkit-nav:start -->
## Project directory

This repository is part of the APIMART open-source AI API toolkit. Browse the complete catalog of provider benchmarks, gateway checks, model examples, and cost tools on the [luyx-66 project profile](https://github.com/luyx-66).
<!-- apimart-toolkit-nav:end -->

## License

MIT
