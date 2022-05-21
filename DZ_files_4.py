import datetime, zipfile
class Zad_4:
    @staticmethod
    def make_file():
        filename = str(datetime.date.today()) + '.txt'
        zipfilename = str(datetime.date.today()) + '.zip'
        with open(filename, 'w', encoding='utf-8') as f_write:
            f_write.write(f'{datetime.date.today()}')
        newzip = zipfile.ZipFile(zipfilename, 'a')
        newzip.write(filename)
        newzip.close()

Zad_4.make_file()