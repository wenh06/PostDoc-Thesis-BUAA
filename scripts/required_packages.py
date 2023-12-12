"""Get the list of required packages from the log file of a compile using full TeXLive."""

import re
from pathlib import Path
from typing import List, Union


def get_required_packages(log_file: Union[Path, str]) -> List[str]:
    pattern = (
        "/[\\w\\-/]+texlive/\\d{4}/texmf-dist/tex/(?:latex|generic)/"
        "(?P<package>[\\w\\-\\._]+)/[\\w\\-/]+\\.(?:sty|def|cfg|clo|fd|ldf|cls|tex)"
    )
    # e.g. /usr/local/texlive/2023/texmf-dist/tex/latex/pgf/systemlayer/pgfsys.sty
    log_content = Path(log_file).read_text().replace("\n", "")
    packages = re.findall(pattern, log_content)
    packages = list(set(packages))
    return packages
