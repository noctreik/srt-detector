import re
import os

import srt


class Detection:

    def __init__(self, srt_file, sentence, detected_word, dt_start, dt_end):
        self.srt_file = srt_file
        self.sentence = sentence
        self.detected_word = detected_word
        self.dt_start = dt_start
        self.dt_end = dt_end

    def __str__(self, ):
        return f"{self.srt_file.split('/')[-1]} - {self.sentence} [{self.detected_word}] @ {self.dt_start}"


def clean_up(text):
    return text.replace("!", "") \
        .replace(".", "") \
        .replace(",", "") \
        .replace("?", "") \
        .lower()


def parse_keywords(keywords_path):
    with open(keywords_path, 'r') as f:
        keywords_set = {x.lower().rstrip() for x in f.readlines()}
    return keywords_set


def detect_keywords(text_, keyword):
    m = re.search(f"(^|\s){keyword}($|\s)", text_)
    if m:
        return True
    return False


def parse_srt(subtitles_folder, keywords_set):
    detected_keywords = []
    srt_files = [f"{subtitles_folder}/{x}" for x in os.listdir(subtitles_folder) if x.endswith(".srt")]

    for srt_file in srt_files:
        print(f"Detecting keywords in: {srt_file}")
        with open(srt_file, "r") as f:
            for sentence in srt.parse(f.read()):
                text = sentence.content
                text_ = clean_up(text)

                for keyword in keywords_set:
                    if detect_keywords(text_, keyword):
                        detection = Detection(srt_file, text, keyword, sentence.start, sentence.end)
                        detected_keywords.append(detection)

    return detected_keywords


def main():
    subtitles_folder = "subtitles"
    keywords_path = "keywords.txt"
    keywords_set = parse_keywords(keywords_path)
    detected_list = parse_srt(subtitles_folder, keywords_set)

    for detected in detected_list:
        print(detected)


if __name__ == '__main__':
    main()
