import dataclasses

from annict_wrapper.utils import check_date_format


@dataclasses.dataclass
class StartedAt:
    dt: str

    def __post_init__(self):
        if not check_date_format(self.dt):
            raise ValueError(f"dt in missed format. correct format is %Y/%m/%d %H:%M.")
