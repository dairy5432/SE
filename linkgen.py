import sys
import os

# 基础 URL (注意中间加上了 /sfx/)
BASE_URL = "https://raw.githubusercontent.com/dairy5432/SE/refs/heads/main/sfx/"
# 结尾的固定参数
END_PARAMS = "=N/A=100=N/A"


def main():
    print("请粘贴文件名列表（包含后缀）。")
    print("粘贴完成后，请**连续按两次回车**（即输入一个空行）来结束输入。")
    print("-" * 50)

    lines = []

    while True:
        try:
            # 读取输入
            line = input()
            stripped_line = line.strip()

            # 如果是空行则结束
            if not stripped_line:
                break

            lines.append(stripped_line)
        except EOFError:
            break

    print("\n" + "=" * 20 + " 生成结果 " + "=" * 20 + "\n")

    for original_text in lines:
        # 使用 os.path.splitext 获取不带后缀的文件名
        # text_no_ext 是文件名， extension 是后缀
        text_no_ext, extension = os.path.splitext(original_text)

        # 按照格式拼接：
        # <去掉后缀>=<BASE_URL><原文件名>=N/A=100=N/A
        result = f"{text_no_ext}={BASE_URL}{original_text}{END_PARAMS}"

        print(result)


if __name__ == "__main__":
    main()