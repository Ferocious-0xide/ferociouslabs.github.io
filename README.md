# Ferocious Labs Website

Edge AI solutions for higher education. Built with FastHTML and hosted on GitHub Pages.

## Project Structure
```
ferociouslabs/
├── .python-version     # Pyenv version file
├── .gitignore         # Git ignore file
├── README.md          # This file
├── requirements.txt   # Python dependencies
├── main.py           # Main FastHTML application
└── static/           # Static assets (images, etc.)
    └── images/       # Image storage
```

## Development Setup

1. Install pyenv if you haven't already:
```bash
# On macOS
brew install pyenv

# On Linux
curl https://pyenv.run | bash
```

2. Add pyenv to your shell configuration:
```bash
# Add to ~/.bashrc or ~/.zshrc
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

3. Install Python and set up the project:
```bash
# Install Python 3.11.5
pyenv install 3.11.5

# Create project directory
mkdir ferociouslabs
cd ferociouslabs

# Set local Python version
pyenv local 3.11.5

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Unix/macOS
# OR
.\venv\Scripts\activate  # On Windows

# Install dependencies
pip install python-fasthtml
pip freeze > requirements.txt
```

4. Set up Git repository:
```bash
git init
git add .
git commit -m "Initial commit"
```

## GitHub Pages Setup

1. Create a new repository on GitHub named `ferociouslabs.github.io`

2. Push your local repository:
```bash
git remote add origin git@github.com:yourusername/ferociouslabs.github.io.git
git branch -M main
git push -u origin main
```

3. In your GitHub repository settings:
   - Go to "Pages"
   - Set branch to "main"
   - Save

## Development

1. Activate virtual environment:
```bash
source venv/bin/activate  # On Unix/macOS
# OR
.\venv\Scripts\activate  # On Windows
```

2. Run the development server:
```bash
python main.py
```

3. Visit `http://localhost:8000` in your browser

## Deployment

Since we're using GitHub Pages, which only serves static content, we'll need to:
1. Generate static HTML from our FastHTML application
2. Commit and push the static files to the repository

You can use the following command to build the static site:
```bash
python build.py  # We'll create this script to generate static HTML
```

## Images and Assets

Store images in the `static/images/` directory. Reference them in your FastHTML application like this:
```python
Img(src="/static/images/your-image.png", alt="Description")
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test locally
4. Submit a pull request

## License

MIT License - See LICENSE file for details