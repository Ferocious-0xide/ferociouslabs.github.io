from fasthtml.common import *

app = FastHTML(hdrs=(picolink,))

def nav_bar():
    return Nav(
        Div(
            A("🦀 Ferocious Labs", href="/", cls="brand"),
            Ul(
                Li(A("Home", href="/")),
                Li(A("Services", href="/services")),
                Li(A("Projects", href="/projects")),
                Li(A("Blog", href="/blog")),
                Li(A("About", href="/about")),
                Li(A("Contact", href="/contact")),
                cls="nav-links"
            ),
            cls="container"
        ),
        cls="nav-main"
    )

def footer():
    return Footer(
        Div(
            Div(
                H4("Ferocious Labs"),
                P("Edge AI Solutions for Higher Education"),
                cls="col",
                style="text-align: left;"
            ),
            Div(
                H4("Connect"),
                P("GitHub: @Ferocious-0xide"),
                P("Email: contact@ferociouslabs.com"),
                cls="col",
                style="text-align: right;"
            ),
            cls="container",
            style="display: flex; justify-content: space-between; align-items: start; padding: 1rem;"
        ),
        P("© 2025 Ferocious Labs - Built with FastHTML", 
          cls="text-center",
          style="margin-top: 1rem; border-top: 1px solid #eee; padding-top: 1rem;"),
        cls="footer",
        style="width: 100%; padding: 2rem 0;"
    )

@app.get("/")
def home():
    return Title("Ferocious Labs - Edge AI Solutions"), Main(
        nav_bar(),
        Article(
            H1("Edge AI Implementation", cls="text-center"),
            P("Empowering higher education with practical edge AI solutions.", cls="lead"),
            Section(
                Div(
                    H2("Why Ferocious Labs?"),
                    P("We combine Python scalability with Rust performance to deliver "
                      "efficient edge AI solutions for educational institutions."),
                    cls="container highlight-box"
                ),
                cls="container"
            ),
            cls="container"
        ),
        footer()
    )

@app.get("/services")
def services():
    services_list = [
        ("Edge AI Implementation", "Custom deployment of AI models optimized for edge computing"),
        ("Performance Optimization", "Rust-powered data engineering for maximum efficiency"),
        ("Training & Workshops", "Comprehensive training for technical staff"),
        ("Architecture Design", "Custom system design for your specific needs")
    ]
    
    return Title("Services - Ferocious Labs"), Main(
        nav_bar(),
        Article(
            H1("Our Services", cls="text-center"),
            Section(
                *[Div(
                    H3(title),
                    P(description),
                    cls="service-card"
                ) for title, description in services_list],
                cls="container services-grid"
            ),
            cls="container"
        ),
        footer()
    )

@app.get("/projects")
def projects():
    return Title("Projects - Ferocious Labs"), Main(
        nav_bar(),
        Article(
            H1("Featured Projects", cls="text-center"),
            Section(
                Div(
                    H3("Edge LLM Deployment"),
                    P("Local language model implementation optimized with Rust"),
                    cls="project-card"
                ),
                Div(
                    H3("Research Computing Platform"),
                    P("High-performance computing environment for academic research"),
                    cls="project-card"
                ),
                cls="container projects-grid"
            ),
            cls="container"
        ),
        footer()
    )

@app.get("/blog")
def blog():
    blog_posts = [
        ("Introduction to Edge AI", "Exploring the benefits of edge computing in education"),
        ("Rust + Python: Better Together", "How we use Rust and Python for optimal performance"),
        ("Local LLMs in Education", "Implementing private language models for universities")
    ]
    
    return Title("Blog - Ferocious Labs"), Main(
        nav_bar(),
        Article(
            H1("Blog", cls="text-center"),
            Section(
                *[Div(
                    H3(title),
                    P(description),
                    A("Read More →", href="#", cls="read-more"),
                    cls="blog-card"
                ) for title, description in blog_posts],
                cls="container blog-grid"
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
                H2("Our Story"),
                P("Ferocious Labs was founded to bridge the gap between cutting-edge AI technology "
                  "and practical implementation in higher education. We combine Python's ecosystem "
                  "with Rust's performance to deliver optimal solutions."),
                H2("Our Approach"),
                P("We believe in empowering institutions to maintain control and privacy of their "
                  "AI systems while building internal capability. Our focus on edge computing and "
                  "local deployment ensures data sovereignty and performance."),
                cls="container about-content"
            ),
            cls="container"
        ),
        footer()
    )

@app.get("/contact")
def contact():
    return Title("Contact - Ferocious Labs"), Main(
        nav_bar(),
        Article(
            H1("Contact Us", cls="text-center"),
            Section(
                P("Interested in implementing edge AI solutions at your institution?"),
                Div(
                    H3("Get In Touch"),
                    P("Email: contact@ferociouslabs.com"),
                    P("GitHub: @Ferocious-0xide"),
                    cls="contact-info"
                ),
                cls="container"
            ),
            cls="container"
        ),
        footer()
    )

if __name__ == "__main__":
    serve(host="0.0.0.0", port=8000)