from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


# Book-level citations shown next to each book title.
BIBLIOGRAPHY: dict[str, str] = {
	"(ced)griffiths": "D. Griffiths. *Intro. to Electrodynamics*, 4th ed.",
	"(ced)jackson": "J. Jackson. *Classical Electrodynamics*, 3rd ed.",
	"(cm)goldstein": "H. Goldstein, C. Poole & J. Safko. *Classical Mechanics*, 3rd ed.",
	"(gr)schutz": "B. Schutz. *A First Course in General Relativity*.",
	"(gr)thooftgr": "G. 't Hooft. *Introduction to General Relativity (lecture notes)*.",
	"(particles)griffiths": "D. Griffiths. *Intro. to Elementary Particles*.",
	"(qft)schwartz": "M. Schwartz. *Quantum Field Theory and the Standard Model*.",
	"(qft)weinberg": "S. Weinberg. *The Quantum Theory of Fields*.",
	"(sstate)kittel": "C. Kittel. *Intro. to Solid State Physics*, 8th ed.",
	"(string)polchinski": "J. Polchinski. *String Theory*, vol. 1 & 2.",
	"(string)thooftstring": "G. 't Hooft. *Introduction to String Theory (lecture notes)*.",
	"(therst)callen": "H. Callen. *Thermodynamics and an Intro. to Thermostatistics*, 2nd ed.",
	"(therst)fermi": "E. Fermi. *Thermodynamics*.",
	"(therst)glazer wark": "M. Glazer & J. Wark. *Stat. Mechanics: A Survival Guide*.",
	"(therst)kittel": "C. Kittel & H. Kroemer. *Thermal Physics*, 2nd ed.",
	"(therst)pathria": "R.K. Pathria & P. Beale. *Statistical Mechanics*.",
}

# Which subject buckets to show, and in what order.
SUBJECT_ORDER: list[str] = [
	"cm",
	"ced",
	"therst",
	"particles",
	"sstate",
	"gr",
	"qft",
	"string",
]

SUBJECT_NAMES: dict[str, str] = {
	"cm": "Classical Mechanics",
	"ced": "Classical Electrodynamics",
	"therst": "Thermal & Statistical Physics",
	"particles": "Particle Physics",
	"sstate": "Solid State Physics",
	"gr": "General Relativity",
	"qft": "Quantum Field Theory",
	"string": "String Theory",
}

# Files/folders to ignore while walking.
IGNORE: set[str] = {
	".DS_Store",
	".git",
	".gitignore",
	".obsidian",
	"createIndex.py",
	"self-study.html",
	"course reference.md",
	"misc",
}


@dataclass(frozen=True)
class Counts:
	pdfs: int = 0


def url_path(repo_rel_path: str) -> str:
	"""URL-encode a repo-relative path while preserving slashes."""
	return quote(repo_rel_path, safe="/", encoding="utf-8", errors="strict")


def parse_subject_abbr(book_dir_name: str) -> str | None:
	# Ex: "(cm)goldstein" -> "cm"
	m = re.match(r"^\(([^)]+)\)", book_dir_name)
	return m.group(1) if m else None


def chapter_sort_key(name: str) -> tuple:
	# Prefer numeric prefixes like "1-...".
	m = re.match(r"^(\d+)-", name)
	if m:
		return (0, int(m.group(1)), name)
	return (1, 10**9, name)


def exercise_sort_key(p: Path) -> tuple:
	# Put files first, then directories.
	if p.is_dir():
		return (2, 10**9, p.name)

	# Prefer exercise naming like <book>_<chapter>_<exercise>.pdf
	parts = p.stem.split("_")
	if len(parts) >= 3:
		ex = parts[2]
		m = re.match(r"^(\d+)", ex)
		if m:
			n = int(m.group(1))
			suffix = ex[m.end() :]
			return (0, n, suffix, p.name)

	return (1, 10**9, p.name)


def list_children(dir_path: Path) -> list[Path]:
	children: list[Path] = []
	for p in dir_path.iterdir():
		if p.name in IGNORE:
			continue
		children.append(p)
	return children


def book_citation(book_dir_name: str) -> str:
	return BIBLIOGRAPHY.get(book_dir_name, book_dir_name)


def build_index(repo_root: Path) -> tuple[list[str], Counts]:
	self_study_dir = repo_root / "self-study"

	# subject -> list of book dirs
	subject_books: dict[str, list[Path]] = {abbr: [] for abbr in SUBJECT_ORDER}

	for book_dir in list_children(self_study_dir):
		if not book_dir.is_dir():
			continue
		subject = parse_subject_abbr(book_dir.name)
		if subject in subject_books:
			subject_books[subject].append(book_dir)

	for subject in subject_books:
		subject_books[subject].sort(key=lambda p: p.name)

	counts = Counts()
	lines: list[str] = []

	for subject in SUBJECT_ORDER:
		books = subject_books.get(subject, [])
		if not books:
			continue

		lines.append(f"## {SUBJECT_NAMES.get(subject, subject)}")
		lines.append("")

		for book_dir in books:
			citation = book_citation(book_dir.name)
			lines.append(f"### {citation}")
			lines.append("")

			chapters = [p for p in list_children(book_dir) if p.is_dir()]
			chapters.sort(key=lambda p: chapter_sort_key(p.name))

			for chapter_dir in chapters:
				items = list_children(chapter_dir)
				items.sort(key=exercise_sort_key)

				pdfs = [p for p in items if p.is_file() and p.suffix.lower() == ".pdf"]

				if not pdfs:
					continue

				lines.append(f"- {chapter_dir.name}")

				for pdf in pdfs:
					rel = (
						Path("self-study") / book_dir.name / chapter_dir.name / pdf.name
					).as_posix()
					url = url_path("/" + rel)

					display = pdf.stem
					parts = pdf.stem.split("_")
					if len(parts) >= 3:
						# exercise <chapter>.<exercise>
						display = f"{parts[1]}.{parts[2]}"
					counts = Counts(pdfs=counts.pdfs + 1)

					lines.append(f"  - Exercise {display}: [pdf]({url})")

				lines.append("")

			lines.append("")

	return lines, counts


def generate() -> None:
	repo_root = Path(__file__).resolve().parents[1]
	out_path = repo_root / "physics-study" / "physics-study.md"

	now = datetime.now(timezone.utc).astimezone()
	generated_at = now.strftime("%Y-%m-%d %H:%M %Z")

	body_lines, counts = build_index(repo_root)

	header = [
		"---",
		"layout: physics-study",
		"title: Physics Self-Study",
		"permalink: /physics-study/",
		"---",
		"# Physics Self-Study",
		"",
		"This page is generated from the `self-study/` folder.",
		f"**Total PDFs linked:** {counts.pdfs}",
		"",
		"",
	]

	footer = [
		"---",
		"",
		f"Last generated: **{generated_at}**.",
		"",
	]

	out_path.parent.mkdir(parents=True, exist_ok=True)
	out_path.write_text("\n".join(header + body_lines + footer), encoding="utf-8")


if __name__ == "__main__":
	generate()