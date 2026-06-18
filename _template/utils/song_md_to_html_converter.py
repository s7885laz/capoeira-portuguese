#!/usr/bin/env python3
"""
Song Markdown to HTML Converter for Capoeira Portuguese Learning App

SPECIALIZED FOR: Converting song lesson .md files to HTML pages

Converts song lesson .md files from the songs/ folder to styled HTML pages
for the learning app. Preserves all content, grammar, vocabulary, and cultural notes.

This converter is specifically designed for song lessons (song-*.md).
It will NOT work for general markdown files.

Usage:
    python song_md_to_html_converter.py                    # Convert all song .md files
    python song_md_to_html_converter.py --file song-name.md  # Convert specific song file
    python song_md_to_html_converter.py --watch             # Watch for new songs and auto-convert
"""

import os
import re
import sys
import glob
import argparse
from pathlib import Path
from datetime import datetime
import time


class MDToHTMLConverter:
    def __init__(self, project_root=None):
        """Initialize converter with project paths."""
        if project_root is None:
            # Auto-detect project root (parent of utils folder)
            project_root = Path(__file__).parent.parent

        self.project_root = Path(project_root)
        self.songs_dir = self.project_root / "songs"
        self.app_dir = self.project_root / "app"
        self.utils_dir = self.project_root / "utils"

        # Verify directories exist
        if not self.songs_dir.exists():
            raise FileNotFoundError(f"Songs directory not found: {self.songs_dir}")
        if not self.app_dir.exists():
            self.app_dir.mkdir(parents=True, exist_ok=True)

    def extract_metadata(self, content):
        """Extract metadata from markdown file."""
        metadata = {
            "title": "Unknown Song",
            "subtitle": "",
            "date": datetime.now().strftime("%B %Y"),
            "status": "In Study",
            "type": "Corrido",
            "difficulty": 2,
            "source": "Traditional"
        }

        # Extract from Basic Info section
        basic_info_match = re.search(
            r'## Basic Info\n(.*?)\n---',
            content,
            re.DOTALL
        )

        if basic_info_match:
            basic_info = basic_info_match.group(1)

            # Extract title (from first H1 if exists)
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if title_match:
                metadata["title"] = title_match.group(1).strip()

            # Extract date
            date_match = re.search(r'Date added: (.+)', basic_info)
            if date_match:
                metadata["date"] = date_match.group(1).strip()

            # Extract status
            status_match = re.search(r'Status: (.+)', basic_info)
            if status_match:
                metadata["status"] = status_match.group(1).strip()

            # Extract type
            type_match = re.search(r'Type: (.+)', basic_info)
            if type_match:
                metadata["type"] = type_match.group(1).strip()

            # Extract source
            source_match = re.search(r'Source: (.+)', basic_info)
            if source_match:
                metadata["source"] = source_match.group(1).strip()

        # Estimate difficulty (default 2, could be parsed from content)
        # For now, use length as proxy: longer = harder
        if len(content) > 15000:
            metadata["difficulty"] = 3
        elif len(content) < 8000:
            metadata["difficulty"] = 1

        return metadata

    def extract_section(self, content, section_name):
        """Extract a section from markdown content."""
        # Match ## Section Name through next ## or end of file
        pattern = rf'## {re.escape(section_name)}\n(.*?)(?=\n## |\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else ""

    def markdown_table_to_html(self, table_text):
        """Convert markdown table to HTML table."""
        lines = table_text.strip().split('\n')
        if len(lines) < 2:
            return ""

        html = '<table>\n<thead>\n<tr>\n'

        # Header row
        headers = [col.strip() for col in lines[0].split('|') if col.strip()]
        for header in headers:
            html += f'<th>{header}</th>\n'
        html += '</tr>\n</thead>\n<tbody>\n'

        # Data rows (skip separator row)
        for line in lines[2:]:
            if not line.strip() or '|' not in line:
                continue
            cells = [col.strip() for col in line.split('|') if col.strip()]
            if cells:
                html += '<tr>\n'
                for i, cell in enumerate(cells):
                    # Bold text in first column (usually keywords)
                    if i == 0 and not cell.startswith('<'):
                        cell = f'<strong>{cell}</strong>'
                    html += f'<td>{cell}</td>\n'
                html += '</tr>\n'

        html += '</tbody>\n</table>\n'
        return html

    def extract_all_tables_from_section(self, section_content):
        """Extract all markdown tables from a section and convert them to HTML."""
        """Returns list of (table_title, html_table) tuples if tables have headers, or just html_table."""
        if not section_content:
            return []

        tables_html = []
        lines = section_content.split('\n')
        current_table_start = None

        for i, line in enumerate(lines):
            if '|' in line and current_table_start is None:
                # Start of a table
                current_table_start = i
            elif current_table_start is not None:
                # Check if table ended
                if (not line.strip() or
                    (not '|' in line and line.strip() and not line.startswith('---'))):
                    # End of table
                    table_text = '\n'.join(lines[current_table_start:i])
                    if table_text.strip():
                        tables_html.append(self.markdown_table_to_html(table_text))
                    current_table_start = None

        # Handle table at end of section
        if current_table_start is not None:
            table_text = '\n'.join(lines[current_table_start:])
            if table_text.strip():
                tables_html.append(self.markdown_table_to_html(table_text))

        return tables_html

    def section_to_html(self, content, section_name, section_type='text'):
        """Convert markdown section to HTML."""
        section_content = self.extract_section(content, section_name)

        if not section_content:
            return ""

        if section_type == 'table':
            return self.markdown_table_to_html(section_content)
        elif section_type == 'lyrics':
            return f'<div class="lyrics-box">{section_content}</div>\n'
        elif section_type == 'text':
            # Convert markdown formatting
            lines = section_content.split('\n')
            html = ""
            for line in lines:
                if line.startswith('### '):
                    html += f"<h3>{line[4:].strip()}</h3>\n"
                elif line.startswith('- '):
                    if not html.endswith('<ul>\n'):
                        html += '<ul style="margin-left: 20px; line-height: 1.8;">\n'
                    html += f"<li>{line[2:].strip()}</li>\n"
                elif line.startswith('*'):
                    if not html.endswith('</ul>\n'):
                        html += '</ul>\n'
                elif line.strip():
                    html += f"<p>{line.strip()}</p>\n"
            if html.endswith('</li>\n'):
                html += '</ul>\n'
            return html

        return section_content

    def slugify(self, text):
        """Convert text to URL-friendly slug."""
        # Convert to lowercase
        slug = text.lower()
        # Replace spaces and special chars with hyphens
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[\s_]+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')

    def get_difficulty_color(self, difficulty):
        """Return CSS class for difficulty level."""
        difficulty_classes = {
            1: 'difficulty-1',
            2: 'difficulty-2',
            3: 'difficulty-3',
            4: 'difficulty-4',
            5: 'difficulty-5'
        }
        return difficulty_classes.get(difficulty, 'difficulty-2')

    def extract_media_links(self, content):
        """Extract media links from markdown content."""
        media_section = self.extract_section(content, 'Media Links')
        if not media_section:
            return []

        links = []
        lines = media_section.split('\n')

        for line in lines:
            # Look for markdown links: [text](url)
            match = re.search(r'\[(.*?)\]\((https?://[^\)]+)\)', line)
            if match:
                text = match.group(1).strip()
                url = match.group(2).strip()
                links.append((text, url))

        return links

    def convert_md_to_html(self, md_file):
        """Convert a single markdown file to HTML."""
        print(f"Converting: {md_file.name}...", end=" ")

        # Read markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract metadata
        metadata = self.extract_metadata(content)

        # Generate HTML filename from title
        html_filename = self.slugify(metadata['title']) + '.html'
        html_path = self.app_dir / html_filename

        # Extract key sections
        media_links = self.extract_media_links(content)
        lyrics_section = self.extract_section(content, 'Lyrics')
        pronunciation_section = self.extract_section(content, 'Pronunciation')
        vocabulary_section = self.extract_section(content, 'Vocabulary')
        grammar_section = self.extract_section(content, 'Grammar Notes')
        cultural_section = self.extract_section(content, 'Cultural Notes')
        practice_section = self.extract_section(content, 'Practice')

        # Build HTML
        html = self._generate_html_template(
            metadata=metadata,
            media_links=media_links,
            lyrics=lyrics_section,
            pronunciation=pronunciation_section,
            vocabulary=vocabulary_section,
            grammar=grammar_section,
            cultural=cultural_section,
            practice=practice_section
        )

        # Write HTML file
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ {html_filename}")
        return html_path

    def _generate_html_template(self, metadata, media_links, lyrics, pronunciation, vocabulary, grammar, cultural, practice):
        """Generate complete HTML page from sections."""

        # Prepare media links
        media_links_html = ""
        if media_links:
            media_links_html += '<div class="media-links">\n'
            for text, url in media_links:
                media_links_html += f'<a href="{url}" class="media-link">{text}</a>\n'
            media_links_html += '</div>\n'

        # Prepare lyrics sections
        lyrics_html = ""
        if lyrics:
            # Extract Full Lyrics section
            full_lyrics_match = re.search(
                r'### Full.*?Lyrics\n(.*?)(?=\n###|\n---|\Z)',
                lyrics,
                re.DOTALL
            )
            if full_lyrics_match:
                lyrics_html += '<h3>Full Portuguese Lyrics</h3>\n'
                lyrics_text = full_lyrics_match.group(1).strip()
                lyrics_html += f'<div class="lyrics-box">{lyrics_text}</div>\n'

            # Extract Line-by-Line Meaning table (case-insensitive)
            line_by_line_match = re.search(
                r'### (?:Line-by-Line|Line-by-line) Meaning\n(.*?)(?=\n###|\n---|\Z)',
                lyrics,
                re.DOTALL
            )
            if line_by_line_match:
                lyrics_html += '<h3>English Translation</h3>\n'
                table_text = line_by_line_match.group(1).strip()
                lyrics_html += self.markdown_table_to_html(table_text)

        # Prepare pronunciation
        pronunciation_html = ""
        if pronunciation:
            # Extract pronunciation table
            tables = self.extract_all_tables_from_section(pronunciation)
            if tables:
                pronunciation_html += tables[0]

            # Extract pronunciation tips or additional text (non-table content)
            lines = pronunciation.split('\n')
            in_table = False
            capture_text = False
            for i, line in enumerate(lines):
                if '|' in line:
                    in_table = True
                elif in_table and (not line.strip() or (not '|' in line and not line.startswith('---'))):
                    in_table = False
                    capture_text = True
                elif capture_text and line.strip():
                    # Format the text content
                    line = re.sub(r'\*\*(.*?)\*\*', r'\1', line)  # Remove markdown bold
                    if line.startswith('- '):
                        if not pronunciation_html.endswith('<ul>\n'):
                            pronunciation_html += '<ul style="margin-top: 15px; margin-left: 20px; line-height: 1.6;">\n'
                        pronunciation_html += f'<li>{line[2:].strip()}</li>\n'
                    elif line.strip():
                        if pronunciation_html.endswith('</li>\n'):
                            pronunciation_html += '</ul>\n'
                        pronunciation_html += f'<p style="margin-top: 15px; font-size: 0.95em; color: #666;">{line.strip()}</p>\n'
            if pronunciation_html.endswith('</li>\n'):
                pronunciation_html += '</ul>\n'

        # Prepare vocabulary
        vocabulary_html = ""
        if vocabulary:
            tables = self.extract_all_tables_from_section(vocabulary)
            if tables:
                vocabulary_html = tables[0]

        # Prepare grammar
        grammar_html = ""
        if grammar:
            # Extract subsections with their content
            subsections = re.findall(
                r'### ([^\n]+)\n(.*?)(?=\n### |\Z)',
                grammar,
                re.DOTALL
            )
            for sub_title, sub_content in subsections:
                grammar_html += f'<h3>{sub_title.strip()}</h3>\n'
                # Extract all tables from this subsection
                tables = self.extract_all_tables_from_section(sub_content)
                if tables:
                    for table in tables:
                        grammar_html += table
                else:
                    # No table, handle as text
                    for line in sub_content.split('\n'):
                        if line.strip() and not line.startswith('|') and not line.startswith('---'):
                            if line.startswith('- '):
                                grammar_html += f'<p>{line[2:].strip()}</p>\n'
                            elif line.strip():
                                grammar_html += f'<p>{line.strip()}</p>\n'

        # Prepare cultural notes
        cultural_html = ""
        if cultural:
            # Convert text content to paragraphs
            lines = cultural.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('- '):
                    cultural_html += f'<p>{line[2:]}</p>\n'
                elif line and not line.startswith('-'):
                    cultural_html += f'<p>{line}</p>\n'

        # Prepare practice
        practice_html = ""
        if practice:
            lines = practice.split('\n')
            in_list = False
            for line in lines:
                if re.match(r'^\d+\.', line):
                    if not in_list:
                        practice_html += '<ol>\n'
                        in_list = True
                    practice_html += f'<li>{line.lstrip("0123456789. ").strip()}</li>\n'
                elif in_list and not line.strip():
                    practice_html += '</ol>\n'
                    in_list = False
                elif in_list and line.startswith('   '):
                    # Nested item or continuation
                    practice_html += f'<li style="margin-left: 20px;">{line.strip()}</li>\n'
            if in_list:
                practice_html += '</ol>\n'

        # Build complete HTML
        difficulty_class = self.get_difficulty_color(metadata['difficulty'])

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata['title']} - Capoeira Portuguese Learning</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 20px;
        }}
        .header h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            color: #666;
            font-size: 1.1em;
        }}
        .meta {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin: 20px 0;
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
        }}
        .meta-item {{
            text-align: center;
        }}
        .meta-label {{
            color: #999;
            font-size: 0.9em;
            text-transform: uppercase;
        }}
        .meta-value {{
            color: #667eea;
            font-weight: bold;
            font-size: 1.1em;
        }}
        .section {{
            margin: 40px 0;
        }}
        .section h2 {{
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 20px;
            border-left: 4px solid #667eea;
            padding-left: 15px;
        }}
        .section h3 {{
            color: #764ba2;
            font-size: 1.3em;
            margin-top: 25px;
            margin-bottom: 15px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }}
        th {{
            background: #667eea;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        td {{
            padding: 12px;
            border-bottom: 1px solid #eee;
        }}
        tr:hover {{
            background: #f9f9f9;
        }}
        .lyrics-box {{
            background: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #764ba2;
            font-style: italic;
            line-height: 1.8;
            margin: 20px 0;
            white-space: pre-wrap;
        }}
        .pronunciation {{
            background: #fff3cd;
            padding: 15px;
            border-radius: 6px;
            margin: 15px 0;
            border-left: 4px solid #ffc107;
        }}
        .pronunciation-text {{
            font-weight: 600;
            color: #333;
            margin-bottom: 5px;
        }}
        .pronunciation-guide {{
            color: #666;
            font-style: italic;
        }}
        .cultural-note {{
            background: #e7f3ff;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            margin: 20px 0;
        }}
        .cultural-note p {{
            margin-bottom: 12px;
            line-height: 1.6;
        }}
        .vocab-badge {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
        }}
        .practice-box {{
            background: #f0fff4;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #28a745;
            margin: 20px 0;
        }}
        .practice-box h4 {{
            color: #28a745;
            margin-bottom: 10px;
        }}
        .practice-box ol, .practice-box ul {{
            margin-left: 20px;
        }}
        .practice-box li {{
            margin-bottom: 10px;
            line-height: 1.6;
        }}
        .media-links {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
        }}
        .media-link {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 10px 15px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.95em;
            transition: background 0.3s;
        }}
        .media-link:hover {{
            background: #764ba2;
        }}
        .nav-buttons {{
            display: flex;
            gap: 15px;
            margin-top: 40px;
            justify-content: space-between;
        }}
        .btn {{
            padding: 12px 24px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            transition: background 0.3s;
            text-align: center;
        }}
        .btn-back {{
            background: #6c757d;
            color: white;
            flex: 1;
        }}
        .btn-back:hover {{
            background: #5a6268;
        }}
        .btn-quiz {{
            background: #28a745;
            color: white;
            flex: 1;
        }}
        .btn-quiz:hover {{
            background: #218838;
        }}
        .difficulty {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
        }}
        .{difficulty_class} {{
            background: {self._get_difficulty_bg(metadata['difficulty'])};
            color: {self._get_difficulty_text(metadata['difficulty'])};
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{metadata['title']}</h1>
            <p>{metadata['subtitle']}</p>
        </div>

        <div class="meta">
            <div class="meta-item">
                <div class="meta-label">Type</div>
                <div class="meta-value">{metadata['type']}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Difficulty</div>
                <div class="meta-value"><span class="difficulty {difficulty_class}">{metadata['difficulty']}/5</span></div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Status</div>
                <div class="meta-value">{metadata['status']}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Added</div>
                <div class="meta-value">{metadata['date']}</div>
            </div>
        </div>

        <!-- Media Links -->
        <div class="section">
            <h2>🎵 Listen</h2>
            {media_links_html}
        </div>

        <!-- Lyrics -->
        <div class="section">
            <h2>📝 Lyrics</h2>
            {lyrics_html}
        </div>

        <!-- Pronunciation -->
        <div class="section">
            <h2>🔊 Pronunciation</h2>
            {pronunciation_html}
        </div>

        <!-- Vocabulary -->
        <div class="section">
            <h2>📚 Vocabulary</h2>
            {vocabulary_html}
        </div>

        <!-- Grammar -->
        <div class="section">
            <h2>📖 Grammar</h2>
            {grammar_html}
        </div>

        <!-- Cultural Context -->
        <div class="section">
            <h2>🌍 Cultural Context</h2>
            <div class="cultural-note">
                {cultural_html}
            </div>
        </div>

        <!-- Practice -->
        <div class="section">
            <div class="practice-box">
                <h4>✏️ Practice Exercises</h4>
                {practice_html}
            </div>
        </div>

        <!-- Navigation -->
        <div class="nav-buttons">
            <a href="poc.html" class="btn btn-back">← Back to Home</a>
            <a href="#" class="btn btn-quiz">Take Quiz →</a>
        </div>
    </div>
</body>
</html>
"""
        return html

    def _get_difficulty_bg(self, level):
        """Get background color for difficulty level."""
        colors = {
            1: '#d4edda',
            2: '#cfe2ff',
            3: '#fff3cd',
            4: '#f8d7da',
            5: '#f5c2c7'
        }
        return colors.get(level, '#cfe2ff')

    def _get_difficulty_text(self, level):
        """Get text color for difficulty level."""
        colors = {
            1: '#155724',
            2: '#084298',
            3: '#664d03',
            4: '#842029',
            5: '#842029'
        }
        return colors.get(level, '#084298')

    def convert_all(self):
        """Convert all markdown files to HTML."""
        md_files = list(self.songs_dir.glob('song-*.md'))

        if not md_files:
            print(f"No song files found in {self.songs_dir}")
            return 0

        print(f"Found {len(md_files)} song files. Converting...\n")
        converted = 0

        for md_file in sorted(md_files):
            try:
                self.convert_md_to_html(md_file)
                converted += 1
            except Exception as e:
                print(f"✗ Error converting {md_file.name}: {e}")

        print(f"\n✓ Successfully converted {converted}/{len(md_files)} files")
        return converted

    def convert_single(self, filename):
        """Convert a single file by name."""
        md_file = self.songs_dir / filename

        if not md_file.exists():
            print(f"✗ File not found: {filename}")
            return 0

        try:
            self.convert_md_to_html(md_file)
            return 1
        except Exception as e:
            print(f"✗ Error: {e}")
            return 0

    def watch_and_convert(self, interval=5):
        """Watch songs folder for new files and convert automatically."""
        print(f"Watching {self.songs_dir} for new songs (Ctrl+C to stop)...\n")
        converted_files = set()

        try:
            while True:
                md_files = set(self.songs_dir.glob('song-*.md'))
                new_files = md_files - converted_files

                for md_file in new_files:
                    try:
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] ", end="")
                        self.convert_md_to_html(md_file)
                        converted_files.add(md_file)
                    except Exception as e:
                        print(f"✗ Error: {e}")

                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n\n✓ Watch mode stopped")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Capoeira song lesson Markdown files to HTML"
    )
    parser.add_argument(
        "--file",
        help="Convert specific file (e.g., song-ai-ai-aide.md)"
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch songs folder for new files and auto-convert"
    )
    parser.add_argument(
        "--project",
        help="Project root directory (auto-detected if not specified)"
    )

    args = parser.parse_args()

    try:
        converter = MDToHTMLConverter(project_root=args.project)

        if args.watch:
            converter.watch_and_convert()
        elif args.file:
            converted = converter.convert_single(args.file)
            sys.exit(0 if converted else 1)
        else:
            converted = converter.convert_all()
            sys.exit(0 if converted else 1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
