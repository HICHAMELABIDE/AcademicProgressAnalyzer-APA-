grades = []

# Collect 7 grades with validation
for i in range(1, 8):
    while True:
        try:
            grade = float(input(f"Enter grade N{i} (0-20): "))
            if 0 <= grade <= 20:
                grades.append(grade)
                break  # Exit loop if valid
            else:
                print("❌ Error! Grade must be between 0 and 20.")
        except ValueError:  # Handle non-numeric inputs
            print("❌ Invalid input. Please enter a number.")

# Calculate average
average = sum(grades) / len(grades)
print(f"\n📊 The student's average is: {average:.2f}")

# Determine academic mention
if average < 10:
    mention = "Insufficient"
elif average < 12:
    mention = "Passable"
elif average < 14:
    mention = "Good"
elif average < 16:
    mention = "Very Good"
else:
    mention = "Excellent"

print(f"🏅 Academic mention: {mention}")