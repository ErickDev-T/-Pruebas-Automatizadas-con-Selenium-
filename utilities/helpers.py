import os

def take_screenshot(driver, filename):
    # Crear la ruta absoluta basada en la ubicación del archivo helpers.py
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Subir al directorio raíz del proyecto (sube de /utilities a /)
    project_root = os.path.dirname(base_path)

    screenshots_dir = os.path.join(project_root, "reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    filepath = os.path.join(screenshots_dir, f"{filename}.png")

    driver.save_screenshot(filepath)
    print(f"Screenshot guardado en: {filepath}")
