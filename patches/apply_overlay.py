from pathlib import Path


ASSET_VERSION = "5"
LS_CSS = f'<link rel="stylesheet" href="/static/zh-overlay/ls-zh.css?v={ASSET_VERSION}">'
LS_CONFIG = """window.LS_ZH_OVERLAY = {
      enabled: true,
      debug: false,
      lang: "zh-CN"
    };"""
LS_JS = f'<script src="/static/zh-overlay/ls-zh.js?v={ASSET_VERSION}"></script>'


def insert_once(text: str, anchor: str, snippet: str, *, after: bool = True) -> str:
    if snippet in text:
        return text
    idx = text.find(anchor)
    if idx == -1:
        raise RuntimeError(f"anchor not found: {anchor}")
    pos = idx + len(anchor) if after else idx
    return text[:pos] + snippet + text[pos:]


def patch_base_template(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = insert_once(
        text,
        '<link href="{{settings.FRONTEND_HOSTNAME}}/react-app/main.css?v={{ versions.backend.commit }}" rel="stylesheet">',
        "\n    " + LS_CSS,
    )
    text = insert_once(
        text,
        '<script nonce="{{request.csp_nonce}}">\n',
        "    " + LS_CONFIG + "\n",
    )
    text = insert_once(
        text,
        "{% endblock %}\n\n<div id=\"dynamic-content\">",
        f"  {LS_JS}\n",
        after=False,
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def patch_simple_template(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = insert_once(
        text,
        '<link href="{{settings.HOSTNAME}}{% static \'css/main.css\' %}" rel="stylesheet"/>',
        "\n  " + LS_CSS,
    )
    text = insert_once(
        text,
        "</body>",
        f'  <script nonce="{{{{request.csp_nonce}}}}">\n    {LS_CONFIG}\n  </script>\n  {LS_JS}\n',
        after=False,
    )
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    patch_base_template(Path("/label-studio/label_studio/templates/base.html"))
    patch_simple_template(Path("/label-studio/label_studio/templates/simple.html"))


if __name__ == "__main__":
    main()
