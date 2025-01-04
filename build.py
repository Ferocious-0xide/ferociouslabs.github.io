import os
import shutil
from main import app
from starlette.testclient import TestClient

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def build_site():
    client = TestClient(app)
    routes = ['/', '/projects', '/about']
    
    # Create or clear docs directory
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    os.makedirs('docs')
    
    # Build HTML pages
    for route in routes:
        response = client.get(route)
        
        # Determine output path
        if route == '/':
            output_path = 'docs/index.html'
        else:
            output_path = f'docs{route}/index.html'
        
        # Ensure directory exists
        ensure_dir(output_path)
        
        # Write the HTML
        with open(output_path, 'w') as f:
            f.write(response.text)
    
    # Copy CNAME file to docs directory
    with open('CNAME', 'r') as source:
        with open('docs/CNAME', 'w') as target:
            target.write(source.read())
    
    # Copy static directory if it exists
    if os.path.exists('static'):
        shutil.copytree('static', 'docs/static', dirs_exist_ok=True)
    
    print("Static site built successfully!")

if __name__ == "__main__":
    build_site()