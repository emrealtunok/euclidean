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

def write_distances_to_file(file_path, distances, min_distance):
    """
    Mesafeleri ve minimum mesafeyi bir dosyaya yazar.
    """
    with open(file_path, 'w') as file:
        file.write("Mesafeler:\n")
        for i, distance in enumerate(distances):
            file.write(f"{i+1}. Mesafe: {distance:.4f}\n")
        file.write(f"\nMinimum Mesafe: {min_distance:.4f}")

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
            distances.append(distance)

    # Minimum mesafeyi bul
    min_distance = min(distances)

    # Çıktıyı dosyaya yaz
    write_distances_to_file(output_file, distances, min_distance)

if __name__ == "__main__":
    main()
