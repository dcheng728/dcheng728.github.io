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
	# Prefer numeric prefixes like "1-..." or "1_...".
	m = re.match(r"^(\d+)[_-](.+)$", name)
	if m:
		chapter_num = int(m.group(1))
		tail = m.group(2).replace("_", " ").strip()
		return (0, chapter_num, tail.lower(), name)
	return (1, 10**9, name.lower())


def chapter_display_name(dir_name: str) -> str:
	"""Make chapter folder names human-readable.

	Supports both legacy formats like "1-foo" and the newer "1_foo".
	"""
	chapter_index = dir_name.split("_")[0]
	chapter_name = dir_name[len(chapter_index) + 1 :]
	print(chapter_index, chapter_name)

	m = re.match(r"^(\d+)[_-](.+)$", dir_name)
	if not m:
		return dir_name
	chapter_num = int(m.group(1))
	title = m.group(2).replace("_", " ")
	title = re.sub(r"\s+", " ", title).strip()
	# Important: Avoid leading "1." patterns in list items like "- 1. Title",
	# which Markdown parses as a nested ordered list (the number becomes a marker,
	# not text). Render the number as formatted text instead.
	num_text = f"**{chapter_num}.**"
	return f"{num_text} {title}" if title else num_text


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
			book_lines: list[str] = []
			book_pdfs = 0

			chapters = [p for p in list_children(book_dir) if p.is_dir()]
			chapters.sort(key=lambda p: chapter_sort_key(p.name))

			for chapter_dir in chapters:
				items = list_children(chapter_dir)
				items.sort(key=exercise_sort_key)

				pdfs = [p for p in items if p.is_file() and p.suffix.lower() == ".pdf"]

				if not pdfs:
					continue

				book_lines.append(f"- {chapter_display_name(chapter_dir.name)}")

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
					book_pdfs += 1
					book_lines.append(f"  - Exercise {display}: [PDF]({url}).")

				book_lines.append("")

			book_lines.append("")

			if book_pdfs == 0:
				continue

			lines.append(f"### {citation} ({book_pdfs} worked solutions)")
			lines.append("")
			lines.extend(book_lines)

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
    	"Between 2023 and 2024, I was not enrolled in a formal physics program.",
		"",
    	"For about one year, I self-studied physics using established textbooks.",
		"",
    	"This page served to demonstrate my understanding in physics, in lieu of an institutional transcript.",
		"",
    	"It contains my solutions to textbook exercises, signed and dated.",
		"",
    	"Later (Sep. 2024), I enrolled in the MSc Physics program at Imperial College London.",
		"",
		f"**Total worked solutions:** {counts.pdfs} PDFs.",
		"",
		"",
	]

	footer = [
		"---",
		"",
		f"Last updated: **{generated_at}**.",
		"",
	]

	out_path.parent.mkdir(parents=True, exist_ok=True)
	out_path.write_text("\n".join(header + body_lines + footer), encoding="utf-8")


if __name__ == "__main__":
	generate()