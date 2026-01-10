#!/usr/bin/env python3
"""
动态标语生成器
为 GitHub README 生成基于时间和随机的欢迎语
"""

import random
from datetime import datetime

def get_time_based_greeting():
    """根据当前时间生成问候语"""
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning, explorer."
    elif hour < 18:
        return "Good afternoon, builder."
    else:
        return "Good evening, visionary."

def get_random_cyberpunk_quote():
    """随机选择一个赛博朋克风格的标语"""
    quotes = [
        "Wake up, Neo... The Matrix has you.",
        "Building minds that build minds.",
        "From first principles to AGI.",
        "Code is law.",
        "Decentralize everything.",
        "The singularity is nearer.",
        "Intelligence, amplified.",
        "There is no spoon.",
        "Follow the white rabbit.",
        "The future is already here.",
    ]

    return random.choice(quotes)

def main():
    """主函数：生成并输出完整的欢迎语"""
    time_greeting = get_time_based_greeting()
    quote = get_random_cyberpunk_quote()

    # 组合成完整的欢迎语
    full_greeting = f"{time_greeting} {quote}"

    # 输出（会被 GitHub Actions 捕获）
    print(full_greeting)

if __name__ == "__main__":
    main()
