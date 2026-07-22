"""Text, image, and video request examples for a unified AI API gateway."""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.request


def build_payload(kind: str, model: str, prompt: str, duration: int = 5) -> tuple[str, dict]:
    if kind == "chat":
        return "/chat/completions", {"model": model, "messages": [{"role": "user", "content": prompt}]}
    if kind == "image":
        return "/images/generations", {"model": model, "prompt": prompt, "size": "1:1", "n": 1}
    if kind == "video":
        return "/videos/generations", {"model": model, "prompt": prompt, "duration": duration, "aspect_ratio": "16:9"}
    raise ValueError(f"Unsupported kind: {kind}")


def request_json(url: str, api_key: str, payload: dict | None = None) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8") if payload is not None else None,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST" if payload is not None else "GET",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def task_id(response: dict) -> str | None:
    return response.get("task_id") or response.get("id") or response.get("data", {}).get("task_id")


def wait_for_task(base_url: str, api_key: str, identifier: str, interval: float = 3) -> dict:
    while True:
        result = request_json(f"{base_url.rstrip('/')}/tasks/{identifier}", api_key)
        status = str(result.get("status") or result.get("data", {}).get("status", "")).lower()
        if status in {"completed", "succeeded", "success", "failed", "error"}:
            return result
        time.sleep(interval)


def main() -> None:
    parser = argparse.ArgumentParser(description="Call chat, image, and video models through one gateway.")
    parser.add_argument("kind", choices=("chat", "image", "video"))
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--duration", type=int, default=5)
    parser.add_argument("--wait", action="store_true")
    parser.add_argument("--base-url", default=os.getenv("AI_API_BASE_URL", "https://api.apimart.ai/v1"))
    args = parser.parse_args()
    api_key = os.getenv("APIMART_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        parser.error("Set APIMART_API_KEY or OPENAI_API_KEY in the environment")

    path, payload = build_payload(args.kind, args.model, args.prompt, args.duration)
    result = request_json(f"{args.base_url.rstrip('/')}{path}", api_key, payload)
    identifier = task_id(result)
    if args.wait and identifier:
        result = wait_for_task(args.base_url, api_key, identifier)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
