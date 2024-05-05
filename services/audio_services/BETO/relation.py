
def compare_graphs(intensity1, intensity2):
    # Asegurarse de que las intensidades tienen la misma longitud
    len1 = len(intensity1)
    len2 = len(intensity2)
    if len1 > len2:
        intensity1 = intensity1[:len2]
    elif len1 < len2:
        intensity2 = intensity2[:len1]

    # Aplanar los arrays
    intensity1 = intensity1.flatten()
    intensity2 = intensity2.flatten()

    # Asegurarse de que las intensidades tienen la misma longitud después de aplanar
    len1 = len(intensity1)
    len2 = len(intensity2)
    if len1 > len2:
        intensity1 = intensity1[:len2]
    elif len1 < len2:
        intensity2 = intensity2[:len1]

    # Calcular la correlación cruzada
    correlation = np.correlate(intensity1, intensity2, mode='valid')[0]

    # Calcular el porcentaje de similitud
    similarity_percentage = correlation / max(np.sum(intensity1 * 2), np.sum(intensity2 * 2))

    # Calcular el margen de error
    error_margin = np.std(intensity1 - intensity2)

    return similarity_percentage * 100, error_margin
