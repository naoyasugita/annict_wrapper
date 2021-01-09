import pytest
from annict_wrapper.model.cast import Cast
from annict_wrapper.model.character import Character
from annict_wrapper.model.episode import Episode
from annict_wrapper.model.episode import NextEpisode
from annict_wrapper.model.episode import PrevEpisode
from annict_wrapper.model.organization import Organization
from annict_wrapper.model.people import People
from annict_wrapper.model.program import Program
from annict_wrapper.model.series import Series
from annict_wrapper.model.staff import Staff
from annict_wrapper.model.work import Work
from annict_wrapper.model.work import WorkId


@pytest.fixture
def fixture_cast(fixture_work, fixture_character, fixture_people):
    cast_dict = {
        "id": 12345,
        "name": "テスト太郎",
        "name_en": "Test, Taro",
        "sort_number": 1,
        "work": fixture_work["work_dict"],
        "character": fixture_character["character_dict"],
        "person": fixture_people["people_dict"],
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
def fixture_episode(fixture_work, fixture_prev_episode, fixture_next_episode):
    episode_dict = {
        "id": 45,
        "number": None,
        "number_text": "第1話",
        "sort_number": 1,
        "title": "test1",
        "records_count": 0,
        "record_comments_count": 0,
        "work": fixture_work["work_dict"],
        "prev_episode": fixture_prev_episode["prev_episode_dict"],
        "next_episode": fixture_next_episode["next_episode_dict"],
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


@pytest.fixture
def fixture_organization():
    organization_dict = {
        "id": 3,
        "name": "P.A.WORKS",
        "name_kana": "ぴーえーわーくす",
        "name_en": "P.A.WORKS",
        "url": "http://www.pa-works.jp/",
        "url_en": "https://www.pa-works.jp/en/",
        "wikipedia_url": "https://ja.wikipedia.org/wiki/%E3%83%94%E3%83%BC%E3%82%A8%E3%83%BC%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B9",
        "wikipedia_url_en": "",
        "twitter_username": "PAWORKS_info",
        "twitter_username_en": "PAWORKS_eng",
        "favorite_organizations_count": 81,
        "staffs_count": 23,
    }
    organization = Organization.from_dict(organization_dict=organization_dict)
    yield {"organization": organization, "organization_dict": organization_dict}


@pytest.fixture
def fixture_people():
    people_dict = {
        "id": 1234,
        "name": "テスト",
        "name_kana": "てすと",
        "name_en": "te, suto",
        "nickname": "てすとん",
        "nickname_en": "",
        "gender_text": "女性",
        "url": "hogehoge1234.html",
        "url_en": "",
        "wikipedia_url": "http://hogehoge/%E6%9D%B1%E5%B1%B1%E5%A5%88%E5%A4%AE",
        "wikipedia_url_en": "",
        "twitter_username": "test",
        "twitter_username_en": "",
        "birthday": "1995-12-02",
        "blood_type": "b",
        "height": 154,
        "favorite_people_count": 74,
        "casts_count": 58,
        "staffs_count": 0,
        "prefecture": {"id": 13, "name": "東京都"},
    }
    people = People.from_dict(people_dict=people_dict)
    yield {"people": people, "people_dict": people_dict}


@pytest.fixture
def fixture_work():
    work_dict = {
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
    }

    work = Work.from_dict(work_dict = work_dict)
    yield {"work": work, "work_dict": work_dict}


@pytest.fixture
def fixture_work_movie():
    work_dict = {
        "id": 1234,
        "title": "テストワーク",
        "title_kana": "てすとわーく",
        "media": "movie",
        "media_text": "映画",
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
    }

    work = Work.from_dict(work_dict = work_dict)
    yield {"work": work, "work_dict": work_dict}


@pytest.fixture
def fixture_program(fixture_work, fixture_episode):
    program_dict = {
        "id": 35387,
        "started_at": "2016-05-07T20:10:00.000Z",
        "is_rebroadcast": False,
        "channel": {"id": 4, "name": "日本テレビ"},
        "work": fixture_work["work_dict"],
        "episode": fixture_episode["episode_dict"],
    }
    program = Program.from_dict(program_dict=program_dict)
    yield {"program": program, "program_dict": program_dict}


@pytest.fixture
def fixture_series():
    series_dict = {
        "id": 12,
        "name": "テスト",
        "name_ro": "test",
        "name_en": "test",
    }
    series = Series(**series_dict)
    yield {"series": series, "series_dict": series_dict}


@pytest.fixture
def fixture_staff_when_org(fixture_work, fixture_organization):
    work = fixture_work["work_dict"]
    organization = fixture_organization["organization_dict"]

    # print(work)
    staff_dict = {
        "id": 35319,
        "name": "京都アニメーション",
        "name_en": "",
        "role_text": "アニメーション制作",
        "role_other": "",
        "role_other_en": "",
        "sort_number": 200,
        "work": work,
        "organization": organization,
        "person": None,
    }
    print("🍷" * 20)
    # print(staff_dict)
    # print("🍷" * 20)
    staff = Staff.from_dict(staff_dict=staff_dict)
    print(staff)
    print("🍷" * 20)
    yield {"staff": staff, "staff_dict": staff_dict}


@pytest.fixture
def fixture_staff_when_person(fixture_work, fixture_people):
    staff_dict = {
        "id": 35319,
        "name": "京都アニメーション",
        "name_en": "",
        "role_text": "アニメーション制作",
        "role_other": "",
        "role_other_en": "",
        "sort_number": 200,
        "work": fixture_work["work_dict"],
        "organization": None,
        "person": fixture_people["people_dict"],
    }
    staff = Staff.from_dict(staff_dict=staff_dict)
    yield {"staff": staff, "staff_dict": staff_dict}
