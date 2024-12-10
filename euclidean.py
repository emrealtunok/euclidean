def euclidean_distance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon.
    """
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def read_points_from_file(file_path):
    """
    Noktaları bir dosyadan okur ve bir liste olarak döndürür.
    """
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def write_distances_to_file(file_path, distances, min_distance, min_points):
    """
    Mesafeleri, noktalarla birlikte ve minimum mesafeyi bir dosyaya yazar.
    """
    with open(file_path, 'w') as file:
        file.write("Mesafeler:\n")
        for i, (distance, point1, point2) in enumerate(distances):
            file.write(f"{i+1}. Mesafe: {distance:.4f} (Noktalar: {point1} -> {point2})\n")
        file.write(f"\nMinimum Mesafe: {min_distance:.4f} (Noktalar: {min_points[0]} -> {min_points[1]})")

def main():
    # Giriş ve çıkış dosyalarının yolları
    input_file = "input.txt"
    output_file = "output.txt"

    # Noktaları dosyadan oku
    points = read_points_from_file(input_file)

    # Mesafeleri hesapla
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            distances.append((distance, points[i], points[j]))

    # Minimum mesafeyi bul
    min_distance, min_point1, min_point2 = min(distances, key=lambda x: x[0])

    # Çıktıyı dosyaya yaz
    write_distances_to_file(output_file, distances, min_distance, (min_point1, min_point2))

if __name__ == "__main__":
    main()
