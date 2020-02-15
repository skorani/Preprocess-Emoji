# -*- encoding: utf-8 -*-

from flashtext import KeywordProcessor

from emojies_data import UNICODE_EMOJI


def replace(text):
    kwp = KeywordProcessor()
    kwp.non_word_boundaries = set()
    kwp.add_keywords_from_dict(
        {" {} ".format(v): [k] for k, v in UNICODE_EMOJI.items()}
    )

    clean_text = kwp.replace_keywords(text).strip()

    return clean_text
