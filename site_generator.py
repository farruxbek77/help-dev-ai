# Professional Site Generator - Pro Max Edition

def generate_html(site_name, site_type, site_color, site_description, image1_url, image2_url):
    """Pro Max HTML generator with 2 images and full description"""
    
    # Rangni CSS formatiga o'tkazish
    color_map = {
        'ko\'k': '#3498db', 'qizil': '#e74c3c', 'yashil': '#2ecc71',
        'sariq': '#f39c12', 'binafsha': '#7c3aed', 'qora': '#2c3e50',
        'oq': '#ecf0f1', 'pushti': '#ff69b4', 'to\'q ko\'k': '#1e40af',
        'jigarrang': '#8b4513', 'kulrang': '#6b7280', 'moviy': '#0ea5e9'
    }
    main_color = color_map.get(site_color.lower(), '#7c3aed')
    
    # Tavsifni bo'laklarga ajratish
    paragraphs = site_description.split('\n')
    description_html = '\n'.join([f'                    <p>{p.strip()}</p>' for p in paragraphs if p.strip()])
    
    html_code = f'''<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name} - Professional Website Pro Max</title>
    <meta name="description" content="{site_description[:150]}...">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --primary: {main_color};
            --primary-light: #a78bfa;
            --bg-dark: #0a0118;
            --text-light: #e2e8f0;
            --text-gray: #94a3b8;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
            line-height: 1.6;
            color: var(--text-light);
            background: var(--bg-dark);
        }}
        
        .navbar {{
            background: rgba(10, 1, 24, 0.95);
            backdrop-filter: blur(20px);
            padding: 1.2rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(167, 139, 250, 0.15);
        }}
        
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        
        .navbar .container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary-light) 0%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .nav-links {{ display: flex; list-style: none; gap: 2.5rem; }}
        .nav-links a {{ color: #cbd5e1; text-decoration: none; transition: 0.3s; }}
        .nav-links a:hover {{ color: var(--primary); }}
        
        .hero {{
            padding: 160px 0 100px;
            text-align: center;
            min-height: 85vh;
            display: flex;
            align-items: center;
            background: radial-gradient(ellipse at top, rgba(124, 58, 237, 0.15) 0%, transparent 50%), var(--bg-dark);
        }}
        
        .hero-title {{
            font-size: 5rem;
            font-weight: 900;
            margin-bottom: 2rem;
            background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 50%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -3px;
            animation: fadeInUp 0.8s ease;
        }}
        
        .hero-subtitle {{
            font-size: 1.5rem;
            color: var(--text-gray);
            margin-bottom: 3rem;
            animation: fadeInUp 0.8s ease 0.2s both;
        }}
        
        .hero-image {{
            max-width: 600px;
            width: 100%;
            height: auto;
            border-radius: 20px;
            margin: 3rem auto;
            box-shadow: 0 20px 60px rgba(124, 58, 237, 0.4);
            border: 2px solid rgba(167, 139, 250, 0.15);
            animation: fadeInUp 0.8s ease 0.3s both;
        }}
        
        .btn {{
            display: inline-block;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
            color: white;
            padding: 18px 56px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 700;
            transition: all 0.3s;
            box-shadow: 0 10px 40px rgba(124, 58, 237, 0.5);
            animation: fadeInUp 0.8s ease 0.4s both;
        }}
        
        .btn:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(124, 58, 237, 0.7);
        }}
        
        .about {{
            padding: 100px 0;
            background: rgba(15, 10, 31, 0.5);
        }}
        
        .about-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }}
        
        .about-text h2 {{
            font-size: 3rem;
            margin-bottom: 2rem;
            color: #ffffff;
            font-weight: 800;
        }}
        
        .about-text p {{
            font-size: 1.1rem;
            line-height: 1.8;
            color: var(--text-gray);
            margin-bottom: 1.5rem;
        }}
        
        .about-image {{
            width: 100%;
            height: auto;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(124, 58, 237, 0.3);
            border: 2px solid rgba(167, 139, 250, 0.15);
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3rem;
            margin-top: 5rem;
        }}
        
        .stat-item {{
            text-align: center;
            padding: 2.5rem 2rem;
            background: rgba(124, 58, 237, 0.08);
            border-radius: 20px;
            border: 1px solid rgba(167, 139, 250, 0.15);
            transition: all 0.3s;
        }}
        
        .stat-item:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(124, 58, 237, 0.3);
        }}
        
        .stat-item h3 {{
            font-size: 3.5rem;
            color: var(--primary-light);
            font-weight: 900;
        }}
        
        footer {{
            background: rgba(10, 1, 24, 0.8);
            padding: 3rem 0;
            border-top: 1px solid rgba(167, 139, 250, 0.15);
            text-align: center;
        }}
        
        .premium-badge {{
            display: inline-block;
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-top: 1rem;
        }}
        
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @media (max-width: 768px) {{
            .hero-title {{ font-size: 2.8rem; }}
            .nav-links {{ display: none; }}
            .about-content {{ grid-template-columns: 1fr; }}
            .stats {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">{site_name}</div>
            <ul class="nav-links">
                <li><a href="#home">Bosh sahifa</a></li>
                <li><a href="#about">Biz haqimizda</a></li>
                <li><a href="#contact">Aloqa</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero" id="home">
        <div class="container">
            <h1 class="hero-title">{site_name}</h1>
            <p class="hero-subtitle">{site_type}</p>
            <img src="{image1_url}" alt="{site_name}" class="hero-image">
            <a href="#about" class="btn">Batafsil ma'lumot</a>
            
            <div class="stats">
                <div class="stat-item">
                    <h3>100+</h3>
                    <p>Mijozlar</p>
                </div>
                <div class="stat-item">
                    <h3>500+</h3>
                    <p>Loyihalar</p>
                </div>
                <div class="stat-item">
                    <h3>24/7</h3>
                    <p>Yordam</p>
                </div>
            </div>
        </div>
    </section>

    <section class="about" id="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>Biz haqimizda</h2>
{description_html}
                </div>
                <div>
                    <img src="{image2_url}" alt="About" class="about-image">
                </div>
            </div>
        </div>
    </section>

    <footer id="contact">
        <div class="container">
            <p>&copy; 2024 {site_name}. Barcha huquqlar himoyalangan.</p>
            <span class="premium-badge">⭐ Pro Max Premium</span>
        </div>
    </footer>
</body>
</html>'''
    
    return html_code
