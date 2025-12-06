import os

file_path = r'c:\Users\Trabajo_Oficina\OneDrive\Documents\Ingenieria de Sistemas\PortafolioUno\style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

exclude_ranges = [
    (662, 771),
    (845, 869),
    (1685, 1711),
    (1764, 1789),
    (1988, 2001)
]

new_lines = []
for i, line in enumerate(lines):
    exclude = False
    for start, end in exclude_ranges:
        if start <= i <= end:
            exclude = True
            break
    if not exclude:
        new_lines.append(line)

consolidated_block = """
/* Consolidated Responsive Design */
@media (max-width: 1024px) {
    .hero-content {
        grid-template-columns: 1fr;
        text-align: center;
        gap: var(--spacing-xl);
    }

    .hero-image {
        order: -1;
        margin-bottom: var(--spacing-lg);
    }

    .image-container {
        width: 300px;
        height: 300px;
    }

    .hero-buttons {
        justify-content: center;
    }

    .hero-social {
        justify-content: center;
    }

    .about-content {
        grid-template-columns: 1fr;
    }

    .skills-grid {
        grid-template-columns: 1fr;
    }

    .projects-grid {
        grid-template-columns: 1fr;
    }

    .contact-content {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .nav-menu {
        position: fixed;
        top: 70px;
        left: -100%;
        flex-direction: column;
        background: var(--bg-secondary);
        width: 100%;
        padding: var(--spacing-xl);
        transition: var(--transition-normal);
        box-shadow: var(--shadow-lg);
        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }

    .nav-menu.active {
        left: 0;
    }

    .hamburger {
        display: flex;
    }

    .hero-name {
        font-size: 2.5rem;
    }

    .hero-title {
        font-size: 1.5rem;
    }

    .section-title {
        font-size: 2rem;
    }

    .skill-items {
        grid-template-columns: repeat(2, 1fr);
    }

    .certifications-grid {
        grid-template-columns: 1fr;
    }

    .tab-buttons {
        flex-direction: column;
    }

    /* Projects Horizontal Scroll */
    .projects-scroll-container {
        padding: 0 40px;
    }

    .scroll-btn {
        width: 40px;
        height: 40px;
        font-size: 1rem;
    }

    .project-card {
        min-width: 320px;
    }

    .projects-horizontal .project-card {
        min-width: 300px !important;
        max-width: 300px !important;
    }

    .projects-horizontal .project-card .project-image {
        height: 180px !important;
    }

    /* Experience Tabs */
    .experience-tabs .tab-buttons {
        grid-template-columns: 1fr;
        gap: var(--spacing-sm);
    }

    .timeline {
        padding-left: var(--spacing-xl);
    }

    .timeline-dot {
        left: -36px;
    }
}

@media (max-width: 480px) {
    .hero-name {
        font-size: 2rem;
    }

    .hero-title {
        font-size: 1.2rem;
    }

    .hero-buttons {
        flex-direction: column;
        width: 100%;
    }

    .btn {
        width: 100%;
        justify-content: center;
    }

    .image-container {
        width: 250px;
        height: 250px;
    }

    /* Projects Horizontal Scroll */
    .projects-scroll-container {
        padding: 0 30px;
    }

    .project-card {
        min-width: 280px;
    }

    .projects-horizontal .project-card {
        min-width: 260px !important;
        max-width: 260px !important;
    }

    .projects-horizontal .project-card .project-image {
        height: 160px !important;
    }

    .contact-content-centered .social-link {
        width: 45px !important;
        height: 45px !important;
    }
}
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
    f.write(consolidated_block)

print("Successfully updated style.css")
