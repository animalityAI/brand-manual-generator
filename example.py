# Example usage of the Brand Manual Generator

from brand_manual_generator import BrandManualGenerator

# Create a brand manual for a sample brand
generator = BrandManualGenerator(
    brand_name="Acme Corporation",
    primary_color="#FF5722",
    secondary_color="#2196F3",
    font_primary="Roboto",
    font_secondary="Lato"
)

# Save the brand manual
filepath = generator.save_brand_manual()
print(f"Example brand manual generated at: {filepath}")
