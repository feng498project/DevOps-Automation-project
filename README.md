# Python Backup Script + GitHub Actions CI

This project includes a Python script for backing up folders and a basic GitHub Actions CI workflow that runs flake8 lint checks on Python file updates.

## 🔁 Features

- Backup any folder to a specified destination
- Timestamped backup naming
- GitHub Actions pipeline to ensure code quality (linting)

## 🛠 Requirements

- Python 3.10+
- GitHub repository for CI

## ▶️ Usage

```bash
python backup.py
```

Enter source and destination paths when prompted.

## ⚙️ GitHub Actions

- On every push involving a `.py` file, flake8 is run.
- Edit `.github/workflows/python-backup.yml` to customize behavior.

## 📄 License

MIT License © 2025 Your Name
