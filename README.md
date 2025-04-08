# Knitting Generator

This Python program generates custom crochet patterns based on user specifications, such as measurements and yarn type. It offers a solution for creating patterns that fit individual body types, eliminating the need to purchase multiple patterns for different sizes or adjustments.

## Problem It Solves

Crochet patterns often require specific yarn weights, thread tensions, hooks, and do not conform to all body types. This project uses mathematical calculations to adjust thread tension and stitch size, tailoring patterns to the user's body measurements. This eliminates the need to buy different patterns for each combination of yarn, hook, or body size. Users can also customize their patterns with any yarn, hook, stitch, and thread tension they prefer.

## Features

- Generates crochet patterns tailored to individual body measurements.
- Customizable yarn, stitch, and hook options.
- Adjusts the pattern for a tight, casual, or oversized fit.
- Provides accurate stitch and row measurements based on user-defined swatch data.
- Eliminates the need for multiple patterns by creating a perfectly fitted design.

## How to Use

### Prerequisites

Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Running the Program

1. **Run the Program**:

   - Open the `main.py` file in a Python environment or IDE (e.g., VSCode or PyCharm).
   - You can typically run the file by pressing `F5` or using the terminal with `python main.py`.

2. **Select Your Size**:

   - The program will prompt you to input your size (S, M, L, XL, XXL). Choose a size that is closest to your body measurements.
   - You can adjust individual measurements later if needed.

3. **Adjust Measurements**:

   - If you want to make any measurement adjustments, type `y` and input the values. For each measurement (e.g., bust, waist, hip), enter the value and press enter.
   - Once done, type `s` to save the adjusted measurements.

4. **Choose the Fit**:

   - The program will ask if you want the fit to be tight, casual, or oversized. Follow the prompts to choose your desired fit.
   - The program adjusts the measurements based on this choice using preset values for "ease."

5. **Crochet a Swatch**:

   - Crochet a swatch of at least 4 inches wide and 4 inches tall.
   - The width corresponds to the number of stitches per row, and the height corresponds to the number of rows.

6. **Input Swatch Data**:

   - The program will prompt you to input data about your swatch, including the stitch type used and the dimensions of the swatch.

7. **Generate Your Pattern**:

   - After inputting all necessary data, the generator will output a custom crochet pattern for your sweater.

8. **Pattern Limitations**:
   - The program follows standard crochet pattern conventions but may struggle with rows that repeat multiple times.
   - Updates may be made in the future, but the main goal of this project is to learn Python, so future maintenance is not guaranteed.

## Example Workflow

1. **Input Your Size**:
   - Example: `M` (Medium)
2. **Adjust Measurements (Optional)**:
   - Example: Adjust bust to `40 inches`, sleeve length to `24 inches`.
3. **Choose Fit**:
   - Example: `Casual`
4. **Crochet Swatch**:
   - Example: A 4x4 swatch using `double crochet`.
5. **Input Swatch Data**:
   - Example: `Stitch height: 0.5 inches`, `Stitch width: 0.25 inches`.
6. **Generate Pattern**:
   - Output: The program generates the pattern based on your size, adjustments, and swatch data.

## Files Included

- `measurements.py`: Contains preset body measurements for different sizes and functions for adjusting these measurements.
- `print_bodice.py`: Contains functions for calculating and printing the bodice measurements, including sleeve and neckline shaping.
- `print_rows.py`: Handles row calculations, including increases, decreases, and repeats.
- `quadratics_experiment.py` and `quadratics.py`: Used for calculating parabolic curves to shape the sweater.
- `stitch_swatch_data.py`: Defines stitch types and calculations related to swatch dimensions.
- `sweater_pattern_data.py`: Contains logic for defining sleeve and bodice variables based on swatch data and user measurements.
- `test.py` and `testing.py`: Unit tests for validating the calculations and functionality of the program.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a new feature, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.

---

### Notes

- The program is a work in progress. It was built to learn Python and explore the intersections of mathematics and crochet, so it may not handle every edge case.
- Future updates may improve functionality and expand features based on community feedback.

Happy crocheting! 🌸✨  
