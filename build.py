import os
from main import app
from starlette.testclient import TestClient

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def build_site():
    client = TestClient(app)
    routes = ['/', '/projects', '/about']
    
    # Create docs directory (GitHub Pages uses this or root)
    if not os.path.exists('docs'):
        os.makedirs('docs')
    
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
    
    print("Static site built successfully!")

if __name__ == "__main__":
    build_site()