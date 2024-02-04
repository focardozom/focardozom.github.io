# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# Initialize variables
square_number = 1  # The number of the current square
grains_on_square = 1  # The number of grains on the current square
total_grains = 0  # The total number of grains so far

# Loop through each square on the chessboard
while square_number <= 64:
    # Add the number of grains on the current square to the total
    total_grains += grains_on_square
    # Double the number of grains on the current square for the next square
    grains_on_square *= 2
    # Move to the next square
    square_number += 1

print(f"The total number of grains on the chessboard is: \n {total_grains:,}")

#
#
#
#
#
#
#
#
#
#

# Total number of grains as computed earlier
total_grains = 18446744073709551615

# Weight of a single grain in grams
weight_per_grain = 0.05

# Compute the total weight in grams
total_weight_grams = total_grains * weight_per_grain

# Convert to kilograms
total_weight_kilograms = total_weight_grams / 1000

# Convert to metric tons
total_weight_metric_tons = total_weight_kilograms / 1000

print(f"The total weight of the rice in grams is {total_weight_grams:.2f} grams")
print(f"The total weight of the rice in kilograms is {total_weight_kilograms:.2f} kilograms")
print(f"The total weight of the rice in metric tons is {total_weight_metric_tons:.2f} metric tons")

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
