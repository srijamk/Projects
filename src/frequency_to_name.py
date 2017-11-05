class FrequencyToName():
    wavelengths_and_names = {
    ((3 * 10**9), (3 * 10**12)): "Microwaves",
    ((3 * 10**12), (4.3 * 10**14)): "Infrared Light",
    ((4.3 * 10**14), (7.5 * 10**14)): "Visible Light",
    ((7.5 * 10**14), (3 * 10**17)): "Ultraviolet Light",
    ((3 * 10**17), (3 * 10**19)): "X-Rays"
    }
    def get_name(self, frequency):
