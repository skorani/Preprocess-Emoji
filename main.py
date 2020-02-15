#!/usr/bin/env pythoh
# -*- encoding: utf-8 -*-

import emojies


def main():
    input_text = input("Enter your text:\n")

    no_emoji_text = emojies.replace(input_text)

    print(f"{no_emoji_text}")


if __name__ == "__main__":
    main()
