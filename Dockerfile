FROM heartexlabs/label-studio:1.23.0

USER root

# 注入静态资源
COPY overrides/static/zh-overlay/ls-zh.js /label-studio/label_studio/core/static_build/zh-overlay/ls-zh.js
COPY overrides/static/zh-overlay/ls-zh.css /label-studio/label_studio/core/static_build/zh-overlay/ls-zh.css
COPY patches/apply_overlay.py /tmp/apply_overlay.py
RUN python /tmp/apply_overlay.py && rm -f /tmp/apply_overlay.py

USER 1001
