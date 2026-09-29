"""
Вспомогательный скрипт для генерации скриншотов консоли для Лабораторной работы №1.
Запуск: python scripts/generate_screenshots.py
"""

from pathlib import Path
import io
import sys
from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import lab1


def render_terminal(lines: list[str], output_path: Path, title: str = "PowerShell - python lab1.py") -> None:
    font_size = 18
    line_height = 28
    padding_x = 28
    padding_top = 56
    padding_bottom = 28

    font_path = "C:/Windows/Fonts/consola.ttf"
    font_bold_path = "C:/Windows/Fonts/consolab.ttf"
    font_ui_path = "C:/Windows/Fonts/segoeui.ttf"

    font = ImageFont.truetype(font_path, font_size)
    font_bold = ImageFont.truetype(font_bold_path, font_size)
    font_ui = ImageFont.truetype(font_ui_path, 14)

    max_text_width = 0
    for line in lines:
        bbox = font.getbbox(line)
        w = bbox[2] - bbox[0]
        if w > max_text_width:
            max_text_width = w

    width = max(950, max_text_width + padding_x * 2 + 30)
    height = padding_top + len(lines) * line_height + padding_bottom

    # Окно терминала
    img = Image.new("RGB", (width, height), color="#1e1e24")
    draw = ImageDraw.Draw(img)

    # Заголовок окна
    title_bar_height = 42
    draw.rectangle([(0, 0), (width, title_bar_height)], fill="#18181b")
    draw.line([(0, title_bar_height), (width, title_bar_height)], fill="#2a2a32", width=1)

    # Кнопки управления окном
    btn_y = title_bar_height // 2
    draw.ellipse([(18, btn_y - 6), (30, btn_y + 6)], fill="#ff5f56")
    draw.ellipse([(38, btn_y - 6), (50, btn_y + 6)], fill="#ffbd2e")
    draw.ellipse([(58, btn_y - 6), (70, btn_y + 6)], fill="#27c93f")

    # Текст заголовка
    t_bbox = font_ui.getbbox(title)
    t_w = t_bbox[2] - t_bbox[0]
    draw.text(((width - t_w) // 2, (title_bar_height - (t_bbox[3] - t_bbox[1])) // 2 - 2), title, font=font_ui, fill="#9da5b4")

    # Рабочая область терминала
    draw.rectangle([(0, title_bar_height + 1), (width, height)], fill="#141416")

    # Отрисовка строк с цветовым оформлением
    y = padding_top
    for line in lines:
        cur_font = font
        fill_color = "#dcdfe4"

        trimmed = line.strip()
        if trimmed.startswith("PS "):
            cur_font = font_bold
            fill_color = "#61afef"
        elif trimmed.startswith("==="):
            fill_color = "#5c6370"
        elif "ЛАБОРАТОРНАЯ РАБОТА" in trimmed or "Все 17 заданий" in trimmed:
            cur_font = font_bold
            fill_color = "#98c379"
        elif "Языки программирования для задач ИИ" in trimmed:
            cur_font = font_bold
            fill_color = "#e5c07b"
        elif trimmed.startswith("--- Задание"):
            cur_font = font_bold
            fill_color = "#61afef"
        elif "успешно пройдены" in trimmed or "пройдены!" in trimmed:
            fill_color = "#98c379"
        elif "Вывод" in trimmed or "Магические" in trimmed:
            fill_color = "#c678dd"

        draw.text((padding_x, y), line, font=cur_font, fill=fill_color)
        y += line_height

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, quality=95)
    print(f"Сгенерирован скриншот: {output_path} ({width}x{height})")


def main():
    captured = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured
    lab1.main()
    sys.stdout = old_stdout
    output_lines = captured.getvalue().strip().splitlines()

    screenshots_dir = PROJECT_ROOT / "screenshots"

    # Полный вывод
    full_lines = ["PS C:\\Users\\1\\Desktop\\Python_Lab_1_Ml> python lab1.py"] + output_lines
    render_terminal(full_lines, screenshots_dir / "console_full.png", "PowerShell - python lab1.py (Все задания 1-17)")

    # Блок 1 (Задания 1-9)
    part1_lines = ["PS C:\\Users\\1\\Desktop\\Python_Lab_1_Ml> python lab1.py --tasks 1-9"]
    for line in output_lines:
        if "--- Задание 10:" in line:
            break
        part1_lines.append(line)
    render_terminal(part1_lines, screenshots_dir / "console_tasks_1_9.png", "PowerShell - Задания 1-9")

    # Блок 2 (Задания 10-17)
    part2_lines = ["PS C:\\Users\\1\\Desktop\\Python_Lab_1_Ml> python lab1.py --tasks 10-17"]
    found_10 = False
    for line in output_lines:
        if "--- Задание 10:" in line:
            found_10 = True
        if found_10:
            part2_lines.append(line)
    render_terminal(part2_lines, screenshots_dir / "console_tasks_10_17.png", "PowerShell - Задания 10-17")


if __name__ == "__main__":
    main()
