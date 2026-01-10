#!/usr/bin/env python3
"""
Matrix风格动态标语生成器
为 GitHub README 生成基于时间和随机的欢迎语
"""

import random
from datetime import datetime

def get_time_based_greeting():
    """根据当前时间生成问候语"""
    hour = datetime.now().hour

    if hour < 6:
        return "> Initializing night protocols..."
    elif hour < 12:
        return "> Good morning, Operator."
    elif hour < 18:
        return "> Accessing mainframe..."
    else:
        return "> The Matrix has you..."

def get_random_matrix_quote():
    """随机选择一个黑客帝国风格的标语"""
    quotes = [
        "Wake up, Neo... The Matrix has you.",
        "Follow the white rabbit.",
        "There is no spoon.",
        "Free your mind.",
        "I know kung fu.",
        "The One has arrived.",
        "You take the red pill, you stay in Wonderland.",
        "What is the Matrix? Control.",
        "Dodge this.",
        "Welcome to the real world.",
        "Everything that has a beginning has an end.",
        "The answer is out there, Neo.",
        "You are The One.",
        "Remember... all I'm offering is the truth.",
        "Choice. The problem is choice.",
        "He is beginning to believe.",
        "I can only show you the door. You're the one that has to walk through it.",
        "To deny our own impulses is to deny the very thing that makes us human.",
        "You've been living in a dream world, Neo.",
        "Never send a human to do a machine's job.",
    ]

    return random.choice(quotes)

def main():
    """主函数：生成并输出完整的欢迎语"""
    time_greeting = get_time_based_greeting()
    quote = get_random_matrix_quote()

    # 组合成完整的欢迎语
    full_greeting = f"{time_greeting} {quote}"

    # 输出（会被 GitHub Actions 捕获）
    print(full_greeting)

if __name__ == "__main__":
    main()
