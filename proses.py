class NilaiProcessor:
    def tentukan_grade(self, nilai):
        if nilai >= 85:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 55:
            return "C"
        else:
            return "D"
