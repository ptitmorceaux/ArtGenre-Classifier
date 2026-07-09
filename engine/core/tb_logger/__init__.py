from .writer import (
    write_training_logs,
    write_images,
    write_markdown_from_dict,
)

from .experiment import get_experiment_md
from .training import get_training_md
from .evaluation import get_evaluation_md


def get_summary_md_dict() -> dict[str, str]:
    summary = {}

    summary.update(get_experiment_md())
    summary.update(get_training_md())
    summary.update(get_evaluation_md())

    return summary