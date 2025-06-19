import csv
import matplotlib.pyplot as plt

def plot_bar_from_csv(filepath, x_columns, y_column):
    x_labels = []
    y_values = []

    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # skip header

        rows = [row for row in reader]

    rows.sort(key=lambda row : int(row[2]))
    rows.sort(key=lambda row : int(row[1]))

    for row in rows:
        try:
            x_label = ' '.join(row[i] for i in x_columns)
            y_value = float(row[y_column])
            x_labels.append(x_label)
            y_values.append(y_value)
        except (IndexError, ValueError) as e:
            print(f"Skipping row due to error: {e}")

    plt.figure(figsize=(10, 6))
    bars = plt.bar(x_labels, y_values)
    for i, item in enumerate(bars):
        item.set_color(['purple', "g", "orange"][(int(i / 3)) % 3])
    plt.xlabel(' '.join(header[i] for i in x_columns))
    plt.ylabel(header[y_column])
    plt.yscale("log")
    plt.title('Comparación de Varianzas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    csv_file_path = "results.csv"

    x_columns = [0, 1, 2]
    y_column = 4

    plot_bar_from_csv(csv_file_path, x_columns, y_column)
