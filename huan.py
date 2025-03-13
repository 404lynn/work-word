text = """你复制的文本内容，这里是一段话。这是另一段话。"""

# 在每个句号后添加换行符
processed_text = text.replace("。", "。\n")

print(processed_text)