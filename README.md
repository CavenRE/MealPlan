# MealPlan

MealPlan is a Python application to help you manage and create meal plans based on nutritional data fetched from CalorieNinjas API. This application allows you to view and manage meals, create new meals, and update nutritional information for various food items.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Main Menu](#main-menu)
  - [Meals](#meals)
  - [Create](#create)
  - [Items](#items)
  - [Update](#update)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```
   git clone git@github.com:CavenRE/MealPlan.git
   cd MealPlan
   ```

2. **Install the required dependencies:**

   Make sure you have Python installed. Then, install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up the configuration file:**

   Copy the `config-example.py` to `config.py` and add your CalorieNinjas API key:

   ```
   cp config-example.py config.py
   ```

   Edit `config.py` and set your API key:

   ```
   API_KEY = 'YOUR_API_KEY_HERE'
   ```

## Usage

Run the main script to start the MealPlan application:

```
python main.py
```

### Main Menu

You will be presented with the main menu options:

```
Select an option:
1] Meals (0)
2] Create
3] Items (40)
4] Update
```

### Meals

This option will eventually list all saved meals. Currently, it is not implemented and will display:

```
Meals functionality is not implemented yet.
```

### Create

This option will guide you through creating a new meal. Currently, it is not implemented and will display:

```
Create functionality is not implemented yet.
```

### Items

This option allows you to view items by category. You will be presented with a sub-menu to select a category:

```
Select a category:
1] Protein
2] Carbs
...
9] Back
```

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with improvements. I might be slow on this as this is a side project for me.

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
