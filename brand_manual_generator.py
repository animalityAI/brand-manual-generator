import os
import argparse
from datetime import datetime

class BrandManualGenerator:
    def __init__(self, brand_name, primary_color, secondary_color, font_primary, font_secondary, logo_path=None):
        self.brand_name = brand_name
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.font_primary = font_primary
        self.font_secondary = font_secondary
        self.logo_path = logo_path
        self.date_generated = datetime.now().strftime("%B %d, %Y")
        
    def generate_css(self):
        """Generate CSS for the brand manual"""
        css = f"""
        :root {{
            --primary-color: {self.primary_color};
            --secondary-color: {self.secondary_color};
            --accent-color: #333333;
            --background-color: #ffffff;
            --text-color: #333333;
            --light-gray: #f5f5f5;
            --medium-gray: #e0e0e0;
            --dark-gray: #888888;
        }}

        @import url('https://fonts.googleapis.com/css2?family={self.font_primary.replace(' ', '+')}:wght@400;700&family={self.font_secondary.replace(' ', '+')}:wght@400;700&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: '{self.font_primary}', sans-serif;
            color: var(--text-color);
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: '{self.font_primary}', sans-serif;
            margin-bottom: 0.8em;
            color: var(--primary-color);
        }}
        
        h1 {{
            font-size: 2.5rem;
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        
        h2 {{
            font-size: 2rem;
            margin-top: 40px;
        }}
        
        h3 {{
            font-size: 1.5rem;
            margin-top: 30px;
        }}
        
        p {{
            margin-bottom: 1em;
            font-family: '{self.font_secondary}', sans-serif;
        }}
        
        .sidebar {{
            position: fixed;
            top: 0;
            left: 0;
            width: 280px;
            height: 100vh;
            background-color: var(--primary-color);
            color: white;
            padding: 20px;
            overflow-y: auto;
        }}
        
        .sidebar-header {{
            margin-bottom: 30px;
            text-align: center;
        }}
        
        .sidebar-header img {{
            max-width: 150px;
            margin-bottom: 10px;
        }}
        
        .sidebar-nav {{
            list-style: none;
        }}
        
        .sidebar-nav li {{
            margin-bottom: 5px;
        }}
        
        .sidebar-nav a {{
            color: white;
            text-decoration: none;
            padding: 8px 10px;
            display: block;
            border-radius: 5px;
            transition: background-color 0.2s;
        }}
        
        .sidebar-nav a:hover {{
            background-color: rgba(255, 255, 255, 0.2);
        }}
        
        .main-content {{
            margin-left: 280px;
            padding: 20px 40px;
        }}
        
        .section {{
            margin-bottom: 50px;
            padding-bottom: 30px;
            border-bottom: 1px solid var(--medium-gray);
        }}
        
        .color-palette {{
            display: flex;
            flex-wrap: wrap;
            margin: 20px 0;
            gap: 20px;
        }}
        
        .color-swatch {{
            width: 150px;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        .color-swatch-display {{
            height: 100px;
        }}
        
        .color-swatch-info {{
            padding: 10px;
            background-color: var(--light-gray);
        }}
        
        .font-example {{
            margin: 20px 0;
            padding: 20px;
            background-color: var(--light-gray);
            border-radius: 5px;
        }}
        
        .platform-section {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .platform-item {{
            background-color: var(--light-gray);
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        .platform-item h4 {{
            margin-top: 0;
            color: var(--primary-color);
        }}
        
        .platform-item img {{
            max-width: 100%;
            margin-top: 10px;
            border: 1px solid var(--medium-gray);
        }}
        
        .logo-guidelines {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 20px 0;
        }}
        
        .logo-variation {{
            text-align: center;
            padding: 20px;
            background-color: var(--light-gray);
            border-radius: 5px;
        }}
        
        .logo-variation img {{
            max-width: 100%;
            max-height: 150px;
            margin-bottom: 10px;
        }}
        
        .spacing-diagram {{
            margin: 20px 0;
            padding: 20px;
            background-color: var(--light-gray);
            border-radius: 5px;
            text-align: center;
        }}
        
        .spacing-diagram img {{
            max-width: 100%;
        }}
        
        .do-dont {{
            display: flex;
            margin: 30px 0;
            gap: 20px;
        }}
        
        .do, .dont {{
            flex: 1;
            padding: 20px;
            border-radius: 5px;
        }}
        
        .do {{
            background-color: rgba(46, 204, 113, 0.1);
            border: 1px solid #2ecc71;
        }}
        
        .dont {{
            background-color: rgba(231, 76, 60, 0.1);
            border: 1px solid #e74c3c;
        }}
        
        .do h4, .dont h4 {{
            text-align: center;
            margin-top: 0;
        }}
        
        .do img, .dont img {{
            max-width: 100%;
            display: block;
            margin: 10px auto;
        }}
        
        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid var(--medium-gray);
            text-align: center;
            font-size: 0.9rem;
            color: var(--dark-gray);
        }}
        
        @media (max-width: 1024px) {{
            .sidebar {{
                width: 220px;
            }}
            
            .main-content {{
                margin-left: 220px;
            }}
        }}
        
        @media (max-width: 768px) {{
            .sidebar {{
                display: none;
            }}
            
            .main-content {{
                margin-left: 0;
            }}
        }}
        """
        return css

    def generate_html(self):
        """Generate HTML for the brand manual"""
        # Create logo HTML based on whether a logo path is provided
        logo_html = f'<img src="{self.logo_path}" alt="{self.brand_name} Logo">' if self.logo_path else f'<h1>{self.brand_name}</h1>'
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.brand_name} Brand Manual</title>
    <style>
{self.generate_css()}
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="sidebar-header">
            {logo_html}
            <h3>{self.brand_name}</h3>
        </div>
        <ul class="sidebar-nav">
            <li><a href="#overview">Brand Overview</a></li>
            <li><a href="#logo">Logo Guidelines</a></li>
            <li><a href="#colors">Color Palette</a></li>
            <li><a href="#typography">Typography</a></li>
            <li><a href="#platforms">Platform Guidelines</a></li>
            <li><a href="#web">Web Guidelines</a></li>
            <li><a href="#mobile">Mobile Guidelines</a></li>
            <li><a href="#visionpro">Vision Pro</a></li>
            <li><a href="#applewatch">Apple Watch</a></li>
            <li><a href="#robots">Robots & AI</a></li>
            <li><a href="#api">API Identity</a></li>
            <li><a href="#seo">SEO Guidelines</a></li>
            <li><a href="#buildings">Physical Spaces</a></li>
        </ul>
    </div>

    <div class="main-content">
        <div class="section" id="overview">
            <h1>{self.brand_name} Brand Manual</h1>
            <p>Welcome to the official brand guidelines for {self.brand_name}. This comprehensive guide ensures consistent representation of our brand across all platforms and touchpoints. Following these guidelines will help maintain brand integrity and recognition.</p>
            <p><strong>Last Updated:</strong> {self.date_generated}</p>
        </div>

        <div class="section" id="logo">
            <h2>Logo Guidelines</h2>
            <p>Our logo is the primary visual identifier of our brand. It should be used consistently across all platforms and materials.</p>
            
            <h3>Logo Variations</h3>
            <div class="logo-guidelines">
                <div class="logo-variation">
                    <h4>Primary Logo</h4>
                    {logo_html}
                    <p>Use whenever possible on light backgrounds</p>
                </div>
                <div class="logo-variation">
                    <h4>Inverted Logo</h4>
                    <div style="background-color: {self.primary_color}; padding: 20px; border-radius: 5px;">
                        {logo_html}
                    </div>
                    <p>Use on dark backgrounds</p>
                </div>
                <div class="logo-variation">
                    <h4>Monochrome Logo</h4>
                    <p>Use when color printing is not available</p>
                </div>
            </div>
            
            <h3>Clear Space</h3>
            <p>Always maintain a clear space around the logo to ensure visibility and impact. The minimum clear space is equal to the height of the logo's x-height.</p>
            
            <h3>Minimum Size</h3>
            <p>To maintain legibility, the logo should never be reproduced smaller than:</p>
            <ul>
                <li>Print: 0.75 inches (19mm) wide</li>
                <li>Digital: 80 pixels wide</li>
            </ul>
            
            <h3>Logo Misuse</h3>
            <div class="do-dont">
                <div class="do">
                    <h4>Do</h4>
                    <p>Use approved logo files</p>
                    <p>Maintain proportions</p>
                    <p>Ensure adequate contrast with backgrounds</p>
                </div>
                <div class="dont">
                    <h4>Don't</h4>
                    <p>Stretch or distort the logo</p>
                    <p>Change the logo colors</p>
                    <p>Add effects like shadows or gradients</p>
                    <p>Place logo on busy backgrounds</p>
                </div>
            </div>
        </div>

        <div class="section" id="colors">
            <h2>Color Palette</h2>
            <p>Our color palette is designed to communicate our brand personality across all touchpoints.</p>
            
            <h3>Primary Colors</h3>
            <div class="color-palette">
                <div class="color-swatch">
                    <div class="color-swatch-display" style="background-color: {self.primary_color};"></div>
                    <div class="color-swatch-info">
                        <p><strong>Primary</strong></p>
                        <p>HEX: {self.primary_color}</p>
                    </div>
                </div>
                <div class="color-swatch">
                    <div class="color-swatch-display" style="background-color: {self.secondary_color};"></div>
                    <div class="color-swatch-info">
                        <p><strong>Secondary</strong></p>
                        <p>HEX: {self.secondary_color}</p>
                    </div>
                </div>
            </div>
            
            <h3>Complementary Colors</h3>
            <div class="color-palette">
                <div class="color-swatch">
                    <div class="color-swatch-display" style="background-color: #333333;"></div>
                    <div class="color-swatch-info">
                        <p><strong>Dark Gray</strong></p>
                        <p>HEX: #333333</p>
                    </div>
                </div>
                <div class="color-swatch">
                    <div class="color-swatch-display" style="background-color: #f5f5f5;"></div>
                    <div class="color-swatch-info">
                        <p><strong>Light Gray</strong></p>
                        <p>HEX: #f5f5f5</p>
                    </div>
                </div>
            </div>
            
            <h3>Color Usage</h3>
            <p>Primary colors should be used for key elements such as headers, calls-to-action, and main interface elements. Secondary colors support the primary palette and can be used for accents and supporting elements.</p>
        </div>

        <div class="section" id="typography">
            <h2>Typography</h2>
            <p>Our typefaces are {self.font_primary} for headings and {self.font_secondary} for body text. These fonts reflect our brand personality and enhance readability across platforms.</p>
            
            <h3>Primary Font: {self.font_primary}</h3>
            <div class="font-example">
                <h1 style="font-family: '{self.font_primary}', sans-serif;">Heading 1</h1>
                <h2 style="font-family: '{self.font_primary}', sans-serif;">Heading 2</h2>
                <h3 style="font-family: '{self.font_primary}', sans-serif;">Heading 3</h3>
                <h4 style="font-family: '{self.font_primary}', sans-serif;">Heading 4</h4>
                <h5 style="font-family: '{self.font_primary}', sans-serif;">Heading 5</h5>
                <h6 style="font-family: '{self.font_primary}', sans-serif;">Heading 6</h6>
            </div>
            
            <h3>Secondary Font: {self.font_secondary}</h3>
            <div class="font-example">
                <p style="font-family: '{self.font_secondary}', sans-serif; font-size: 16px;">Body text regular (16px)</p>
                <p style="font-family: '{self.font_secondary}', sans-serif; font-size: 14px;">Body text small (14px)</p>
                <p style="font-family: '{self.font_secondary}', sans-serif; font-size: 12px;">Caption text (12px)</p>
                <p style="font-family: '{self.font_secondary}', sans-serif; font-weight: bold;">Bold text for emphasis</p>
                <p style="font-family: '{self.font_secondary}', sans-serif; font-style: italic;">Italic text for emphasis</p>
            </div>
            
            <h3>Font Pairing & Hierarchy</h3>
            <p>Use {self.font_primary} for headers and titles to create visual hierarchy. Use {self.font_secondary} for body copy, descriptions, and interface text. Maintain consistent hierarchy in all communications.</p>
        </div>