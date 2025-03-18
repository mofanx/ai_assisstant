#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AI助手脚本 - 通过不同快捷键调用不同AI模型
支持模型：
- Gemini (g+f9)
- Qwen (q+f9)
- QWQ (w+f9)
- Grok (x+f9)
- Baidu (b+f9)
- Zhipu (z+f9)
- Aliyun (a+f9)
- Aliyun Web (l+f9)
"""

import argparse

# 第三方库
import keyboard
import pygame

# 导入自定义模块
from assistant import (
    get_clipboard_content, type_result, cancel_current_chat, clear_possible_char,
    OpenAIAssistant, QwenAssistant, QWQAssistant, OpenAITTS
)

# =========================
# 主函数
# =========================

def main():
    parser = argparse.ArgumentParser(description="AI助手脚本 - 通过不同快捷键调用不同AI模型")
    parser.add_argument("--web", action="store_true", help="启用Qwen的web模式，添加chat_type=search参数")
    parser.add_argument("--model", type=str, default="gemini-2.0-flash", help="指定OpenAI要调用的模型名称")
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 初始化模型实例
    qwen_assistant = QwenAssistant(is_web=args.web)
    qwq_assistant = QWQAssistant()
    openai_assistant = OpenAIAssistant(model_name=args.model)
    gemini_assistant = OpenAIAssistant(model_name="gemini-2.0-flash")
    grok_assistant = OpenAIAssistant(model_name="grok-2")
    baidu_assistant = OpenAIAssistant(model_name="ERNIE-Speed-128K")
    # zhipu_assistant = OpenAIAssistant(model_name="GLM-4-Plus")
    zhipu_assistant = OpenAIAssistant(model_name="GLM-4-Flash")
    # aliyun_assistant = AliyunAssistant(model_name="qwen-max")
    aliyun_assistant = OpenAIAssistant(model_name="qwen-max", provider="aliyun")
    aliyun_web_assistant = OpenAIAssistant(model_name="qwen-max", provider="aliyun", enable_search=True)
    tts_assistant = OpenAITTS()

    
    print("=== AI助手已启动 ===")
    print("支持的快捷键:")
    print("f9+o: 调用OpenAI模型")
    print("f9+g: 调用Gemini模型")
    print("f9+x: 调用Grok模型")
    print("f9+q: 调用Qwen模型")
    print("f9+w: 调用QWQ模型")
    print("f9+b: 调用Baidu模型")
    print("f9+z: 调用Zhipu模型")
    print("f9+a: 调用Aliyun模型")
    print("f9+l: 调用Aliyun Web模型")
    print("f9+1: 调用TTS模型")
    print("esc: 取消当前对话输出")
    print("esc+f9: 退出程序")
    
    # 注册快捷键
    keyboard.add_hotkey('f9+o', lambda: [clear_possible_char(), openai_assistant.chat()])
    keyboard.add_hotkey('f9+g', lambda: [clear_possible_char(), gemini_assistant.chat()])
    keyboard.add_hotkey('f9+x', lambda: [clear_possible_char(), grok_assistant.chat()])
    keyboard.add_hotkey('f9+q', lambda: [clear_possible_char(), qwen_assistant.chat_thread()])
    keyboard.add_hotkey('f9+w', lambda: [clear_possible_char(), qwq_assistant.chat_thread()])
    keyboard.add_hotkey('f9+b', lambda: [clear_possible_char(), baidu_assistant.chat()])
    keyboard.add_hotkey('f9+z', lambda: [clear_possible_char(), zhipu_assistant.chat()])
    keyboard.add_hotkey('f9+a', lambda: [clear_possible_char(), aliyun_assistant.chat()])
    keyboard.add_hotkey('f9+l', lambda: [clear_possible_char(), aliyun_web_assistant.chat()])
    # keyboard.add_hotkey('f9+1', lambda: [clear_possible_char(), tts_assistant.chat()])
    keyboard.add_hotkey('f9+1', lambda: [clear_possible_char(), tts_assistant.text_to_speech()])
    keyboard.add_hotkey('esc', cancel_current_chat)
    
    # 保持脚本运行，等待按键事件
    keyboard.wait('esc+f9')  # 按下 Esc+F9 键退出程序
    print("程序已退出")

if __name__ == "__main__":
    main()
