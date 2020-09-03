import pytest

from annict_wrapper.model.cast import Cast
from annict_wrapper.model.character import Character
from annict_wrapper.model.episode import Episode
from annict_wrapper.model.episode import NextEpisode
from annict_wrapper.model.episode import PrevEpisode


@pytest.fixture
def fixture_cast():
    cast_dict = {
        "id": 12345,
        "name": "テスト太郎",
        "name_en": "Test, Taro",
        "sort_number": 1,
        "work": {
            "id": 1234,
            "title": "テストワーク",
            "title_kana": "てすとわーく",
            "media": "tv",
            "media_text": "TV",
            "released_on": "",
            "released_on_about": "",
            "official_site_url": "http://testhoeghoge.com",
            "wikipedia_url": "http://hogehoge/%E6%9D%B1%E5%B1%B1%E5%A5%88%E5%A4%AE",
            "twitter_username": "test_hogehoge",
            "twitter_hashtag": "テスト",
            "syobocal_tid": "1234",
            "mal_anime_id": "12345",
            "images": {
                "recommended_url": "test.jpg",
                "facebook": {"og_image_url": "test.jpg"},
                "twitter": {
                    "mini_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=mini",
                    "normal_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=normal",
                    "bigger_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=bigger",
                    "original_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=original",
                    "image_url": "",
                },
            },
            "episodes_count": 12,
            "watchers_count": 1234,
            "reviews_count": 11,
            "no_episodes": False,
            "season_name": "2018-winter",
            "season_name_text": "2018年冬",
        },
        "character": {
            "id": 12345,
            "name": "テストキャラ",
            "name_kana": "てすときゃら",
            "name_en": "Test, Chara",
            "nickname": "",
            "nickname_en": "",
            "birthday": "",
            "birthday_en": "",
            "age": "",
            "age_en": "",
            "blood_type": "",
            "blood_type_en": "",
            "height": "",
            "height_en": "",
            "weight": "",
            "weight_en": "",
            "nationality": "",
            "nationality_en": "",
            "occupation": "",
            "occupation_en": "",
            "description": "",
            "description_en": "",
            "description_source": "",
            "description_source_en": "",
            "favorite_characters_count": 10,
            "series": None,
            "kind": "",
        },
        "person": {
            "id": 1234,
            "name": "テストパーソン",
            "name_kana": "てすとぱーそん",
            "name_en": "Test, Person",
            "nickname": "てすとん",
            "nickname_en": "",
            "gender_text": "女性",
            "url": "http://hogehoge.html",
            "url_en": "",
            "wikipedia_url": "http://hogehoge/%E6%9D%B1%E5%B1%B1%E5%A5%88%E5%A4%AE",
            "wikipedia_url_en": "",
            "twitter_username": "",
            "twitter_username_en": "",
            "birthday": "2000-01-01",
            "blood_type": "a",
            "height": 150,
            "favorite_people_count": 11,
            "casts_count": 115,
            "staffs_count": 0,
            "prefecture": None,
        },
    }
    cast = Cast(**cast_dict)
    yield {"cast": cast, "cast_dict": cast_dict}


@pytest.fixture
def fixture_cast_2():
    cast_dict = {
        "id": 123456,
        "name": "テスト太郎2",
        "name_en": "Test, Taro2",
        "sort_number": 1,
        "work": {
            "id": 1234,
            "title": "テストワーク",
            "title_kana": "てすとわーく",
            "media": "tv",
            "media_text": "TV",
            "released_on": "",
            "released_on_about": "",
            "official_site_url": "http://testhoeghoge.com",
            "wikipedia_url": "http://hogehoge/%E6%9D%B1%E5%B1%B1%E5%A5%88%E5%A4%AE",
            "twitter_username": "test_hogehoge",
            "twitter_hashtag": "テスト",
            "syobocal_tid": "1234",
            "mal_anime_id": "12345",
            "images": {
                "recommended_url": "test.jpg",
                "facebook": {"og_image_url": "test.jpg"},
                "twitter": {
                    "mini_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=mini",
                    "normal_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=normal",
                    "bigger_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=bigger",
                    "original_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=original",
                    "image_url": "",
                },
            },
            "episodes_count": 12,
            "watchers_count": 1234,
            "reviews_count": 11,
            "no_episodes": False,
            "season_name": "2018-winter",
            "season_name_text": "2018年冬",
        },
        "character": {
            "id": 123456,
            "name": "テストキャラ2",
            "name_kana": "てすときゃら",
            "name_en": "Test, Chara",
            "nickname": "",
            "nickname_en": "",
            "birthday": "",
            "birthday_en": "",
            "age": "",
            "age_en": "",
            "blood_type": "",
            "blood_type_en": "",
            "height": "",
            "height_en": "",
            "weight": "",
            "weight_en": "",
            "nationality": "",
            "nationality_en": "",
            "occupation": "",
            "occupation_en": "",
            "description": "",
            "description_en": "",
            "description_source": "",
            "description_source_en": "",
            "favorite_characters_count": 10,
            "series": {"id": 123, "name": "Steins;Gate", "name_ro": "", "name_en": "",},
            "kind": "",
        },
        "person": {
            "id": 1234,
            "name": "テストパーソン",
            "name_kana": "てすとぱーそん",
            "name_en": "Test, Person",
            "nickname": "てすとん",
            "nickname_en": "",
            "gender_text": "女性",
            "url": "http://hogehoge.html",
            "url_en": "",
            "wikipedia_url": "http://hogehoge/%E6%9D%B1%E5%B1%B1%E5%A5%88%E5%A4%AE",
            "wikipedia_url_en": "",
            "twitter_username": "",
            "twitter_username_en": "",
            "birthday": "2000-01-01",
            "blood_type": "a",
            "height": 150,
            "favorite_people_count": 11,
            "casts_count": 115,
            "staffs_count": 0,
            "prefecture": {"id": 1, "name": "東京都"},
        },
    }
    cast = Cast(**cast_dict)
    yield {"cast": cast, "cast_dict": cast_dict}


@pytest.fixture
def fixture_character():
    character_dict = {
        "id": 1234,
        "name": "テスト太郎",
        "name_kana": "テストたろう",
        "name_en": "Test, Taro",
        "kind": "HogeHoge",
        "nickname": "テストタロウ",
        "nickname_en": "Test, Taro",
        "birthday": "12月1日",
        "birthday_en": "December 1",
        "age": "18歳",
        "age_en": "18",
        "blood_type": "A型",
        "blood_type_en": "A",
        "height": "177 cm",
        "height_en": "177 cm",
        "weight": "59 kg",
        "weight_en": "59 kg",
        "nationality": "日本",
        "nationality_en": "Japan",
        "occupation": "テストテストテストテスト",
        "occupation_en": "test test test test",
        "description": "サンプル",
        "description_en": "",
        "description_source": " てスト",
        "description_source_en": "",
        "favorite_characters_count": 123,
        "series": {"id": 12, "name": "Steins;Gate", "name_ro": "", "name_en": ""},
    }
    character = Character(**character_dict)
    yield {"character": character, "character_dict": character_dict}


@pytest.fixture
def fixture_character_2():
    character_dict = {
        "id": 12345,
        "name": "テスト太郎2",
        "name_kana": "テストたろう2",
        "name_en": "Test, Taro2",
        "kind": "HogeHoge2",
        "nickname": "テストタロウ2",
        "nickname_en": "Test, Taro2",
        "birthday": "12月1日",
        "birthday_en": "December 1",
        "age": "18歳",
        "age_en": "18",
        "blood_type": "A型",
        "blood_type_en": "A",
        "height": "177 cm",
        "height_en": "177 cm",
        "weight": "59 kg",
        "weight_en": "59 kg",
        "nationality": "日本",
        "nationality_en": "Japan",
        "occupation": "テストテストテストテスト",
        "occupation_en": "test test test test",
        "description": "サンプル",
        "description_en": "",
        "description_source": " てスト",
        "description_source_en": "",
        "favorite_characters_count": 123,
        "series": {"id": 12, "name": "Steins;Gate", "name_ro": "", "name_en": ""},
    }
    character = Character(**character_dict)
    yield {"character": character, "character_dict": character_dict}


@pytest.fixture
def fixture_episode():
    episode_dict = {
        "id": 45,
        "number": None,
        "number_text": "第1話",
        "sort_number": 1,
        "title": "test1",
        "records_count": 0,
        "record_comments_count": 0,
        "work": {
            "id": 1234,
            "title": "テストワーク",
            "title_kana": "てすとわーく",
            "media": "tv",
            "media_text": "TV",
            "released_on": "",
            "released_on_about": "",
            "official_site_url": "http://testhoeghoge.com",
            "wikipedia_url": "http://hogehoge/%E6%9D%B1%E5%B1%B1%E5%A5%88%E5%A4%AE",
            "twitter_username": "test_hogehoge",
            "twitter_hashtag": "テスト",
            "syobocal_tid": "1234",
            "mal_anime_id": "12345",
            "images": {
                "recommended_url": "test.jpg",
                "facebook": {"og_image_url": "test.jpg"},
                "twitter": {
                    "mini_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=mini",
                    "normal_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=normal",
                    "bigger_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=bigger",
                    "original_avatar_url": "https://twitter.com/xxxxxxxxxxx/profile_image?size=original",
                    "image_url": "",
                },
            },
            "episodes_count": 12,
            "watchers_count": 1234,
            "reviews_count": 11,
            "no_episodes": False,
            "season_name": "2018-winter",
            "season_name_text": "2018年冬",
        },
        "prev_episode": None,
        "next_episode": None,
    }
    episode = Episode(**episode_dict)
    yield {"episode": episode, "episode_dict": episode_dict}


@pytest.fixture
def fixture_prev_episode():
    prev_episode_dict = {
        "id": 11,
        "number": None,
        "number_text": "第1話",
        "sort_number": 1,
        "title": "テスト",
        "records_count": 0,
        "record_comments_count": 0,
    }
    prev_episode = PrevEpisode(**prev_episode_dict)
    yield {"prev_episode": prev_episode, "prev_episode_dict": prev_episode_dict}


@pytest.fixture
def fixture_next_episode():
    next_episode_dict = {
        "id": 11,
        "number": None,
        "number_text": "第1話",
        "sort_number": 1,
        "title": "テスト",
        "records_count": 0,
        "record_comments_count": 0,
    }
    next_episode = NextEpisode(**next_episode_dict)
    yield {"next_episode": next_episode, "next_episode_dict": next_episode_dict}
