# Image → ANSI Terminal (High Detail)

Рендеринг изображений в **обычном ANSI-терминале** с максимальной возможной детализацией **без искажения цветов**.

Проект не занимается ASCII-артом и стилизацией — цель исключительно в том, чтобы выжать **максимум реальных деталей** из терминала.

---

## Возможности

- TrueColor (24-bit RGB)
- Символ `▀` (2 вертикальных пикселя на один символ)
- Высококачественный ресайз `LANCZOS`
- Корректные цвета (без квантизации и дизеринга)
- Предсказуемый визуальный результат

---

## Ограничения (важно понимать)

Это **физический предел обычного терминала**:

- 1 символ = 2 пикселя (вертикально)
- Увеличение масштаба терминала **не добавляет деталей**
- Больше качества возможно только через:
  - Kitty graphics protocol
  - SIXEL
  - iTerm inline images

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

## Почему нет параметра «качество»

Потому что в терминале:

- «качество» ≠ масштаб
- качество определяется **способом кодирования**, а не размером

В данном проекте используется **единственный корректный high-quality метод**.

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
- Correct color handling (no quantization, no destructive dithering)
- Predictable, physically accurate output

---

## Limitations (important)

This is the **physical limit of a regular ANSI terminal**:

- 1 character = 2 vertical pixels
- Terminal zoom **does not increase detail**
- Higher quality is only possible via:
  - Kitty graphics protocol
  - SIXEL
  - iTerm inline images

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

## Why there is no “quality” parameter

In terminals:

- “quality” ≠ scale
- quality is defined by the **encoding method**, not by size

This project uses the **only correct high-detail encoding available**.

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

