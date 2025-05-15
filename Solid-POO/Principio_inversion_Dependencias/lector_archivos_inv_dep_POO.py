from abc import ABC, abstractmethod

class DataReader(ABC):
    
    @abstractmethod
    def reader_data(self,file_path):
        pass

class WordDataReader(DataReader):
    
    def reader_data(self, file_path):
        print(f'Leyendo el archivo Word: {file_path}')
        return ['data1','data2','date3']

class CSVDataReader(DataReader):
    def reader_data(self, file_path):
        print(f'Leyendo el archivo CSV: {file_path}')
        return ['data1','data2','data3']

class DataProcessor:
    def __init__(self,datareader: DataReader):
        self.datareader=datareader
    
    def reader_data(self,file_path):
        data=self.datareader.reader_data(file_path)
        print(f'Procesando datos {data}')
        return [d.upper() for d in data]

#caso de uso
file=WordDataReader()
data=DataProcessor(file)
data.reader_data('word_file')

file2=CSVDataReader()
data2=DataProcessor(file2)
data.reader_data('CSV_file')