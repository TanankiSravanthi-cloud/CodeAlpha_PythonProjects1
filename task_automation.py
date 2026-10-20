"""Choose a small file automation task from the console."""
from pathlib import Path
import re
import shutil


def move_jpg_files():
    source_text = input("Enter source folder path: ").strip().strip('"')
    destination_text = input("Enter destination folder path: ").strip().strip('"')
    source = Path(source_text).expanduser()
    destination = Path(destination_text).expanduser()

    if not source.is_dir():
        print("The source folder does not exist.")
        return
    if source.resolve() == destination.resolve():
        print("Source and destination folders must be different.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    moved = 0
    for item in source.iterdir():
        if item.is_file() and item.suffix.lower() == ".jpg":
            target = destination / item.name
            if target.exists():
                print(f"Skipped because destination already has this file: {item.name}")
                continue
            shutil.move(str(item), str(target))
            moved += 1
    print(f"Finished. Moved {moved} JPG file(s).")


def extract_emails():
    source_text = input("Enter path to a .txt file: ").strip().strip('"')
    source = Path(source_text).expanduser()
    if not source.is_file() or source.suffix.lower() != ".txt":
        print("Please provide an existing .txt file.")
        return

    content = source.read_text(encoding="utf-8", errors="ignore")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", content)))
    output = source.with_name("extracted_emails.txt")
    output.write_text("\n".join(emails) + ("\n" if emails else ""), encoding="utf-8")
    print(f"Found {len(emails)} unique email address(es). Saved to: {output}")


def save_webpage_title():
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("This option needs optional packages. Run: python -m pip install requests beautifulsoup4")
        return

    url = input("Enter a webpage URL (include https://): ").strip()
    if not url.startswith(("https://", "http://")):
        print("Please enter a valid http:// or https:// URL.")
        return
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "StudentTitleFetcher/1.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.get_text(" ", strip=True) if soup.title else "(No title found)"
        Path("webpage_title.txt").write_text(f"URL: {url}\nTitle: {title}\n", encoding="utf-8")
        print(f"Saved webpage title to webpage_title.txt: {title}")
    except requests.RequestException as error:
        print(f"Could not retrieve webpage: {error}")


def main():
    print("\n=== Task Automation with Python ===")
    print("1. Move .jpg files from a folder to another folder")
    print("2. Extract email addresses from a .txt file")
    print("3. Get the title of a webpage")
    choice = input("Choose an option (1-3): ").strip()
    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        save_webpage_title()
    else:
        print("Invalid choice. Run again and choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
