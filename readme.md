# Image → ANSI Terminal (High Detail)

Рендеринг изображений в **обычном ANSI-терминале** с максимальной возможной детализацией **без искажения цветов**.

Проект не занимается ASCII-артом и стилизацией — цель исключительно в том, чтобы выжать **максимум реальных деталей** из терминала.

---

Original photo vs terminal output (this project).
<p align="center">
  <img src="https://github.com/user-attachments/assets/500e77a0-1d5f-4e0c-99f8-5dc041f200e5" width="45%" />
  <img src="https://github.com/user-attachments/assets/0a6375da-cf5b-4368-9ec0-931c413c9e00" width="45%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/8a850446-2e7b-4a50-881c-f217c9e57e34" width="45%" />
  <img src="https://github.com/user-attachments/assets/5e747c5d-3cdd-43da-aada-24e31284fd1e" width="45%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/e0c7a36c-88a8-4bb6-b72f-fe4b20d0636c" width="45%" />
  <img src="https://github.com/user-attachments/assets/8ddd1cd6-b332-4631-91a9-510628c14cc8" width="45%" />
</p>
---

## Возможности

- TrueColor (24-bit RGB)
- Символ `▀` (2 вертикальных пикселя на один символ)
- Высококачественный ресайз `LANCZOS`
- Предсказуемый визуальный результат

---

## Ограничения (важно понимать)

Это **физический предел обычного терминала**:

- 1 символ = 2 пикселя (вертикально)
- Увеличение масштаба терминала **не добавляет деталей**
- Больше качества возможно только через:
  - Kitty graphics protocol
  - SIXEL

---

## Требования

- Python **3.8+**
- Терминал с поддержкой **24-bit color (truecolor)**
- Установленные библиотеки:

```bash
pip install opencv-python numpy
```

---

## Запуск

### Базовый запуск

```bash
python ascii.py image.jpg
```

По умолчанию:
- ширина = **120 символов**
- высота рассчитывается автоматически с учётом пропорций

---

### Задание ширины вручную

```bash
python ascii.py image.jpg 160
```

Рекомендации:

| Ширина | Когда использовать |
|------|------------------|
| 80 | маленькие терминалы |
| 120 | оптимальный баланс |
| 160 | высокая детализация |
| 200+ | только если терминал очень широкий |

---

## Принцип работы

1. Изображение загружается без изменения цвета
2. Перевод из BGR в RGB
3. Ресайз с интерполяцией `LANCZOS`
4. Каждые **2 вертикальных пикселя** кодируются в один символ `▀`
   - верхний пиксель → foreground color
   - нижний пиксель → background color

Таким образом:

```
1 символ = 2 пикселя
```

Это максимум, возможный в ANSI.

---

## Частые проблемы

### Картинка выглядит «мыльной»

- уменьшите ширину
- проверьте, что масштаб терминала = 100%
- используйте моноширинный шрифт без сглаживания

---

### Цвета выглядят неправильно

- убедитесь, что терминал поддерживает truecolor
- проверьте переменную окружения:

```bash
echo $COLORTERM
```

Должно быть:

```
truecolor
```

---

## Поддерживаемые терминалы

Работает корректно в:

- kitty
- alacritty
- wezterm
- Windows Terminal
- iTerm2 (macOS)

---

## Лицензия

MIT

---

## Примечание

Если вам нужно **реальное пиксельное качество**, а не ANSI-рендеринг — используйте графические протоколы терминалов (Kitty / SIXEL).

Этот проект честно работает в рамках ограничений текста.



---

# Image → ANSI Terminal (High Detail) — English

Rendering images in a **standard ANSI terminal** with the maximum possible detail **without breaking colors**.

This project is not ASCII art or stylization. The goal is purely to extract **maximum real visual detail** from a text terminal.

---

## Features

- TrueColor (24-bit RGB)
- `▀` character (2 vertical pixels per terminal cell)
- High-quality `LANCZOS` resize

---

## Limitations (important)

This is the **physical limit of a regular ANSI terminal**:

- 1 character = 2 vertical pixels
- Terminal zoom **does not increase detail**
- Higher quality is only possible via:
  - Kitty graphics protocol
  - SIXEL
  
---

## Requirements

- Python **3.8+**
- Terminal with **24-bit truecolor** support
- Dependencies:

```bash
pip install opencv-python numpy
```

---

## Usage

### Basic usage

```bash
python ascii.py image.jpg
```

Defaults:
- width = **120 characters**
- height is calculated automatically to preserve aspect ratio

---

### Custom width

```bash
python ascii.py image.jpg 160
```

Recommendations:

| Width | Use case |
|------|---------|
| 80 | small terminals |
| 120 | optimal balance |
| 160 | high detail |
| 200+ | only for very wide terminals |

---

## How it works

1. Image is loaded without color modification
2. Converted from BGR to RGB
3. Resized using `LANCZOS` interpolation
4. Every **2 vertical pixels** are encoded into one `▀` character:
   - upper pixel → foreground color
   - lower pixel → background color

Result:

```
1 character = 2 pixels
```

This is the maximum possible in ANSI.

---

## Common issues

### Image looks blurry

- reduce width
- ensure terminal zoom is set to 100%
- use a monospace font without excessive smoothing

---

### Colors look wrong

- make sure your terminal supports truecolor
- check environment variable:

```bash
echo $COLORTERM
```

Expected:

```
truecolor
```

---

## Supported terminals

Tested and works correctly in:

- kitty
- alacritty
- wezterm
- Windows Terminal
- iTerm2 (macOS)

---

## Note

If you need **real pixel-perfect image quality**, not ANSI rendering — use graphical terminal protocols (Kitty / SIXEL).

This project operates honestly within text terminal limitations.

