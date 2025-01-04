from fasthtml.common import *

app = FastHTML(hdrs=(picolink,))

def nav_bar():
    return Nav(
        Div(
            A("Ferocious Labs", href="/", cls="brand"),
            Ul(
                Li(A("Projects", href="/projects")),
                Li(A("About", href="/about")),
                cls="nav-links"
            ),
            cls="container"
        ),
        cls="nav-main"
    )

def footer():
    return Footer(
        P("© 2025 Ferocious Labs - Edge AI Solutions for Higher Education"),
        cls="container text-center"
    )

@app.get("/")
def home():
    return Title("Ferocious Labs - Edge AI Solutions"), Main(
        nav_bar(),
        Article(
            H1("Edge AI Implementation", cls="text-center"),
            P("Empowering higher education with practical edge AI solutions.", cls="lead"),
            Section(
                H2("Our Focus"),
                P("We specialize in helping educational institutions deploy and maintain their own edge AI systems, "
                  "providing both the technical expertise and training needed for successful implementation."),
                cls="container"
            ),
            cls="container"
        ),
        footer()
    )

@app.get("/projects")
def projects():
    project_items = [
        ("Edge AI Training Platform", "Custom training programs for university staff and researchers"),
        ("Local LLM Deployment", "Implementing private, efficient language models for educational use"),
        ("Research Computing Optimization", "Maximizing resource utilization in research environments")
    ]
    
    return Title("Projects - Ferocious Labs"), Main(
        nav_bar(),
        Article(
            H1("Projects", cls="text-center"),
            Section(
                *[Div(
                    H3(title),
                    P(description),
                    cls="project-card"
                ) for title, description in project_items],
                cls="container projects-grid"
            ),
            cls="container"
        ),
        footer()
    )

@app.get("/about")
def about():
    return Title("About - Ferocious Labs"), Main(
        nav_bar(),
        Article(
            H1("About Us", cls="text-center"),
            Section(
                H2("Our Mission"),
                P("Ferocious Labs was founded to bridge the gap between cutting-edge AI technology "
                  "and practical implementation in higher education. We believe in empowering "
                  "institutions to maintain control and privacy of their AI systems while building "
                  "internal capability."),
                cls="container"
            ),
            cls="container"
        ),
        footer()
    )

if __name__ == "__main__":
    serve(host="0.0.0.0", port=8000)